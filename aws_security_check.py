import boto3

class AWSSecurityChecker:
    def __init__(self, region='us-east-1'):
        self.s3_client = boto3.client('s3', region_name=region)
        self.rds_client = boto3.client('rds', region_name=region)
        self.ec2_client = boto3.client('ec2', region_name=region)
        self.misconfigurations = []

    def check_s3_buckets(self):
        response = self.s3_client.list_buckets()
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            # Check public access
            try:
                public_access = self.s3_client.get_public_access_block(Bucket=bucket_name)
                if not all(public_access['PublicAccessBlockConfiguration'].values()):
                    self.misconfigurations.append(f"S3 Bucket '{bucket_name}' is publicly accessible")
            except self.s3_client.exceptions.NoSuchPublicAccessBlockConfiguration:
                self.misconfigurations.append(f"S3 Bucket '{bucket_name}' is publicly accessible (no public access block)")
            # Check logging
            logging = self.s3_client.get_bucket_logging(Bucket=bucket_name)
            if 'LoggingEnabled' not in logging:
                self.misconfigurations.append(f"S3 Bucket '{bucket_name}' has logging disabled")
            # Check versioning
            versioning = self.s3_client.get_bucket_versioning(Bucket=bucket_name)
            if 'Status' not in versioning or versioning['Status'] != 'Enabled':
                self.misconfigurations.append(f"S3 Bucket '{bucket_name}' has versioning disabled")

    def check_rds_instances(self):
        response = self.rds_client.describe_db_instances()
        for db in response['DBInstances']:
            db_id = db['DBInstanceIdentifier']
            if db['PubliclyAccessible']:
                self.misconfigurations.append(f"RDS Instance '{db_id}' is publicly accessible")
            if not db['DeletionProtection']:
                self.misconfigurations.append(f"RDS Instance '{db_id}' has deletion protection disabled")
            if db['BackupRetentionPeriod'] == 0:
                self.misconfigurations.append(f"RDS Instance '{db_id}' has backups disabled")

    def check_security_groups(self):
        response = self.ec2_client.describe_security_groups()
        for sg in response['SecurityGroups']:
            sg_id = sg['GroupId']
            for rule in sg['IpPermissions']:
                for ip_range in rule.get('IpRanges', []):
                    if ip_range.get('CidrIp') == '0.0.0.0/0':
                        from_port = rule.get('FromPort', 'All')
                        if from_port in [22, 27017]:
                            self.misconfigurations.append(f"Security Group '{sg_id}' allows public access to port {from_port}")

    def run_checks(self):
        self.check_s3_buckets()
        self.check_rds_instances()
        self.check_security_groups()
        return self.misconfigurations

if __name__ == "__main__":
    REGION = 'eu-north-1'
    checker = AWSSecurityChecker(REGION)
    issues = checker.run_checks()
    if issues:
        print("Misconfigurations found:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No misconfigurations found.")