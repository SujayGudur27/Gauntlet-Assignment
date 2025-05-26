Gauntlet Assignment Documentation
Overview
This document outlines the steps I, Sujay Gudur, performed to complete the Gauntlet assignment for the screening process. The assignment involved setting up an AWS environment, creating resources with intentional misconfigurations, writing a Python script to detect these issues, testing the script, documenting findings in a vulnerability report, and cleaning up resources. The assignment was completed on May 26, 2025, between 8:00 PM and 11:42 PM IST.
Steps Performed
1. Environment Setup

Install Python and AWS CLI:

I confirmed that Python 3.13.3 was installed on my Windows 11 machine.
I installed the AWS CLI (version 2.27.22) and verified it by running:aws --version

Output: aws-cli/2.27.22 Python/3.13.3 Windows/11 exe/AMD64.


Set Up Virtual Environment:

I created a project folder at C:\Users\SHREENIVAS\OneDrive\Documents\Gauntlet.
I created a virtual environment in this folder using:python -m venv venv


I activated the virtual environment with:venv\Scripts\activate


I installed the required package boto3 using:pip install boto3




Configure AWS CLI:

I configured the AWS CLI with the credentials of the IAM user security-audit-user by running:aws configure


I entered the Access Key ID and Secret Access Key from the .csv file downloaded earlier, set the region to eu-north-1, and the output format to json.
I verified the configuration with:aws sts get-caller-identity

Output:{
    "UserId": "AIDXXXXXXXXXXXXXXXXXX",
    "Account": "710428422307",
    "Arn": "arn:aws:iam::710428422307:user/security-audit-user"
}





2. Create IAM User and Access Keys

I logged into the AWS Management Console and navigated to the IAM service.
I created an IAM user named security-audit-user.
I attached the SecurityAudit policy to the user to grant permissions for auditing AWS resources.
I generated access keys for programmatic access:
I selected “Application running outside AWS” as the use case.
I downloaded the .csv file containing the Access Key ID and Secret Access Key.


I verified that the access key was active in the IAM user’s “Security credentials” tab.

3. Create AWS Resources with Misconfigurations
I created the following AWS resources in the eu-north-1 region with intentional misconfigurations as per the assignment requirements:

S3 Bucket:

Navigated to the S3 service in the AWS Console.
Created a bucket named my-test-bucket-shreenivas-2025.
Configured it with the following misconfigurations:
Disabled “Block all public access” to make it publicly accessible.
Disabled server access logging.
Disabled versioning.


Confirmed the bucket was created in eu-north-1.


RDS Instance:

Navigated to the RDS service in the AWS Console.
Created a MySQL database instance using the free tier template.
Named the instance mytestdb.
Configured it with the following misconfigurations:
Set “Public access” to “Yes” to make it publicly accessible.
Disabled deletion protection.
Set backup retention to 0 days to disable backups.


Ensured the instance was created in eu-north-1.
Waited for the instance to become available (took approximately 5 minutes).


Security Group:

Navigated to the EC2 service in the AWS Console.
Created a Security Group named my-test-sg.
Configured it with the following misconfigurations:
Added an inbound rule for MongoDB: Custom TCP, port 27017, source 0.0.0.0/0 (public access).
Added an inbound rule for SSH: SSH, port 22, source 0.0.0.0/0 (public access).


Confirmed the Security Group was created in eu-north-1.



4. Develop and Run the Python Script

I created the script aws_security_check.py in the C:\Users\SHREENIVAS\OneDrive\Documents\Gauntlet directory using Notepad.
The script uses the boto3 library to interact with AWS services (S3, RDS, EC2) and detect misconfigurations.
The script is configured to use AWS CLI credentials (via aws configure) and targets the eu-north-1 region.
I ran the script using:python aws_security_check.py


Output:Misconfigurations found:
- S3 Bucket 'my-test-bucket-shreenivas-2025' is publicly accessible
- S3 Bucket 'my-test-bucket-shreenivas-2025' has logging disabled
- S3 Bucket 'my-test-bucket-shreenivas-2025' has versioning disabled
- RDS Instance 'mytestdb' is publicly accessible
- RDS Instance 'mytestdb' has deletion protection disabled
- RDS Instance 'mytestdb' has backups disabled
- Security Group 'sg-02d220cae690cc61b' allows public access to port 22
- Security Group 'sg-02d220cae690cc61b' allows public access to port 27017


The script successfully detected all expected misconfigurations.

5. Create and Run Unit Tests

I created test_aws_security_check.py to validate the functionality of aws_security_check.py.
The test script includes four test cases:
test_check_s3_buckets: Verifies S3 misconfigurations are detected.
test_check_rds_instances: Verifies RDS misconfigurations are detected.
test_check_security_groups: Verifies Security Group misconfigurations are detected.
test_run_checks: Ensures the overall run_checks method returns issues.


I ran the tests with:python test_aws_security_check.py


Output:....
----------------------------------------------------------------------
Ran 4 tests in 2.345s

OK


All tests passed, confirming the script’s functionality.

6. Create Vulnerability Report (Optional)

I created vulnerability_report.md to document the findings and provide recommendations.
The report includes:
An overview of the script run.
Detailed findings from the script output.
Recommendations to fix each misconfiguration.
A conclusion summarizing the risks and next steps.


The report was saved in the project directory.

7. Clean Up AWS Resources

To avoid incurring charges, I deleted all AWS resources created for the assignment:
S3 Bucket:
Navigated to S3 > Buckets.
Selected my-test-bucket-shreenivas-2025, emptied the bucket, and deleted it.


RDS Instance:
Navigated to RDS > Databases.
Selected mytestdb, deleted it without creating a final snapshot.


Security Group:
Navigated to EC2 > Security Groups.
Selected sg-02d220cae690cc61b and deleted it.





8. Prepare Submission

I gathered all required files:
aws_security_check.py
test_aws_security_check.py
vulnerability_report.md
documentation.md (this document)


I created a ZIP file containing these files:Gauntlet_Assignment_SujayGudur.zip


I drafted an email to submit the assignment, attaching the ZIP file, and plan to send it before the deadline of 5:00 PM IST on May 27, 2025.

Files Included

aws_security_check.py: The main script to check AWS misconfigurations.
test_aws_security_check.py: Unit tests for the script.
vulnerability_report.md: Vulnerability report with findings and recommendations.
documentation.md: This document detailing the steps performed.

Challenges Faced

Initially, the AWS CLI command aws was not recognized in the VSCode terminal due to PATH issues. I resolved this by running everything in CMD, where aws worked.
Ensuring all resources were created in the eu-north-1 region required careful attention to avoid region mismatches.

Conclusion
The assignment was completed successfully, with all misconfigurations detected and validated through unit tests. The documentation provides a comprehensive overview of the process, and all AWS resources have been cleaned up to avoid charges. I am ready to submit the assignment before the deadline.
