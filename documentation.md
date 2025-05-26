Gauntlet Assignment Documentation
Overview
I’m Sujay Gudur, and this document details the steps I took to complete the Gauntlet Assignment for the internship screening process. The assignment required setting up an AWS environment, creating resources with intentional misconfigurations, developing a Python script to identify these issues, testing the script, documenting findings in a vulnerability report, and cleaning up resources. I completed the assignment on May 26, 2025, between 8:00 PM and 11:42 PM IST, ensuring submission before the deadline of 5:00 PM IST on May 27, 2025. This project was a valuable opportunity to demonstrate my technical skills and attention to detail.
Steps Performed
1. Environment Setup
To begin, I configured my development environment on my Windows 11 system to ensure compatibility with AWS services.

Python and AWS CLI Installation: I verified that Python 3.13.3 was installed. I then installed AWS CLI version 2.27.22 and confirmed its functionality by running:
aws --version

Output:
aws-cli/2.27.22 Python/3.13.3 Windows/11 exe/AMD64


Virtual Environment: I created a dedicated project directory at C:\Users\SHREENIVAS\OneDrive\Documents\Gauntlet to organize my work. Within this directory, I set up a virtual environment:
python -m venv venv

I activated it with:
venv\Scripts\activate

Then, I installed the boto3 library for AWS interactions:
pip install boto3


AWS CLI Configuration: I configured the AWS CLI with credentials for the security-audit-user IAM user using:
aws configure

I entered the Access Key ID and Secret Access Key from the downloaded .csv file, set the region to eu-north-1, and chose json as the output format. I verified the configuration with:
aws sts get-caller-identity

Output:
{
    "UserId": "AIDXXXXXXXXXXXXXXXXXX",
    "Account": "710428422307",
    "Arn": "arn:aws:iam::710428422307:user/security-audit-user"
}



2. Create IAM User and Access Keys
I used the AWS Management Console to create an IAM user for programmatic access.

Navigated to the IAM service in the AWS Console.
Created an IAM user named security-audit-user.
Attached the SecurityAudit policy to grant permissions for auditing AWS resources.
Generated access keys, selecting “Application running outside AWS” as the use case, and downloaded the .csv file containing the Access Key ID and Secret Access Key.
Confirmed the access key was active in the IAM user’s “Security credentials” tab.

3. Create AWS Resources with Misconfigurations
I created AWS resources in the eu-north-1 region with intentional misconfigurations as specified in the assignment.

S3 Bucket:

Accessed the S3 service in the AWS Console.
Created a bucket named my-test-bucket-shreenivas-2025.
Configured misconfigurations:
Disabled “Block all public access” to allow public access.
Disabled server access logging.
Disabled versioning.


Verified the bucket was created in eu-north-1.


RDS Instance:

Navigated to the RDS service and created a MySQL database instance using the free tier template.
Named the instance mytestdb.
Introduced misconfigurations:
Enabled “Public access” to make it publicly accessible.
Disabled deletion protection.
Set backup retention to 0 days to disable backups.


Confirmed the instance was created in eu-north-1 after approximately 5 minutes.


Security Group:

In the EC2 service, created a Security Group named my-test-sg.
Added misconfigured inbound rules:
Custom TCP, port 27017 (MongoDB), source 0.0.0.0/0 (public access).
SSH, port 22, source 0.0.0.0/0 (public access).


Ensured the Security Group was created in eu-north-1.



4. Develop and Run the Python Script
I developed aws_security_check.py in the C:\Users\SHREENIVAS\OneDrive\Documents\Gauntlet directory using Notepad. The script leverages boto3 to interact with S3, RDS, and EC2 services in eu-north-1, using credentials from the AWS CLI configuration. I executed the script with:
python aws_security_check.py

Output:
Misconfigurations found:
- S3 Bucket 'my-test-bucket-shreenivas-2025' is publicly accessible
- S3 Bucket 'my-test-bucket-shreenivas-2025' has logging disabled
- S3 Bucket 'my-test-bucket-shreenivas-2025' has versioning disabled
- RDS Instance 'mytestdb' is publicly accessible
- RDS Instance 'mytestdb' has deletion protection disabled
- RDS Instance 'mytestdb' has backups disabled
- Security Group 'sg-02d220cae690cc61b' allows public access to port 22
- Security Group 'sg-02d220cae690cc61b' allows public access to port 27017

The script successfully identified all misconfigurations.
5. Create and Run Unit Tests
To ensure the script’s reliability, I created test_aws_security_check.py with four unit tests:

test_check_s3_buckets: Validates S3 misconfiguration detection.
test_check_rds_instances: Validates RDS misconfiguration detection.
test_check_security_groups: Validates Security Group misconfiguration detection.
test_run_checks: Verifies the main run_checks method.

I ran the tests using:
python test_aws_security_check.py

Output:
....
----------------------------------------------------------------------
Ran 4 tests in 2.345s

OK

All tests passed, confirming the script’s functionality.
6. Create Vulnerability Report
I authored vulnerability_report.md to document the findings and provide actionable recommendations. The report includes:

An overview of the script execution.
Detailed findings from the script output.
Recommendations to address each misconfiguration (e.g., enabling S3 public access block, restricting Security Group rules).
A conclusion summarizing risks and mitigation steps.

The report was saved in the project directory and converted to vulnerability_report.pdf for inclusion in the submission email. The PDF is accessible via my Gauntlet Assignment Repository or directly at Vulnerability Report PDF.
7. Clean Up AWS Resources
To prevent any unintended charges, I deleted all AWS resources created for the assignment:

S3 Bucket: In the S3 Console, I emptied and deleted my-test-bucket-shreenivas-2025.
RDS Instance: In the RDS Console, I deleted mytestdb without a final snapshot.
Security Group: In the EC2 Console, I deleted sg-02d220cae690cc61b.

8. Prepare Submission
I compiled the required deliverables:

aws_security_check.py
test_aws_security_check.py
vulnerability_report.md (and .pdf for the email)
documentation.md (this document)

These files were archived into Gauntlet_Assignment_SujayGudur.zip for submission. I prepared an email with the ZIP file attached, ensuring delivery before the May 27, 2025, 5:00 PM IST deadline.
Files Included

aws_security_check.py: Python script to detect AWS misconfigurations.
test_aws_security_check.py: Unit tests for the script.
vulnerability_report.md: Report detailing findings and recommendations (also as .pdf in the email).
documentation.md: This document outlining the assignment process.

These files are available in my Gauntlet Assignment Repository.
Challenges Faced

AWS CLI Issue: The aws command initially failed in my VSCode terminal due to a PATH configuration issue. I resolved this by switching to the Command Prompt, where the CLI functioned correctly.
Region Consistency: I took care to ensure all resources were created in eu-north-1, double-checking settings to avoid discrepancies.

Conclusion
Completing the Gauntlet Assignment was a rewarding experience that allowed me to apply my skills in AWS, Python, and security auditing. The script successfully identified all misconfigurations, and the unit tests validated its reliability. The documentation and vulnerability report provide a comprehensive overview of my approach and findings. I ensured all AWS resources were deleted to avoid charges and prepared the submission with care. I’m grateful for the opportunity to showcase my abilities and welcome any feedback or further instructions.
