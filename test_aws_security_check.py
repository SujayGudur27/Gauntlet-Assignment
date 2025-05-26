import unittest
from aws_security_check import AWSSecurityChecker

class TestAWSSecurityChecker(unittest.TestCase):
    def setUp(self):
        self.checker = AWSSecurityChecker(region='eu-north-1')

    def test_check_s3_buckets(self):
        self.checker.check_s3_buckets()
        self.assertTrue(any("S3 Bucket" in issue for issue in self.checker.misconfigurations))

    def test_check_rds_instances(self):
        self.checker.check_rds_instances()
        self.assertTrue(any("RDS Instance" in issue for issue in self.checker.misconfigurations))

    def test_check_security_groups(self):
        self.checker.check_security_groups()
        self.assertTrue(any("Security Group" in issue for issue in self.checker.misconfigurations))

    def test_run_checks(self):
        issues = self.checker.run_checks()
        self.assertGreater(len(issues), 0)

if __name__ == '__main__':
    unittest.main()