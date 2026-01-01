## IAM Role for AWS Glue

Purpose:
AWS Glue requires an IAM role to access S3 buckets and write processed data.

Role Type:
Service Role for AWS Glue

Permissions:
- Read data from S3 input bucket
- Write transformed data to S3 output location
- Write logs to Amazon CloudWatch

Usage in Project:
This role is attached to the Glue ETL job to enable secure access
to required AWS resources following the principle of least privilege.
