## Amazon CloudWatch for Monitoring and Logging

Purpose:
Amazon CloudWatch is used to monitor and log the execution of
AWS Lambda functions and AWS Glue ETL jobs.

Usage in Project:
- Lambda execution logs are captured in CloudWatch Logs
- Glue job logs and data quality results are monitored via CloudWatch
- Helps in debugging failures and tracking pipeline execution

Fault Tolerance:
CloudWatch logs assist in identifying failures and enable retry
mechanisms for ETL jobs.
