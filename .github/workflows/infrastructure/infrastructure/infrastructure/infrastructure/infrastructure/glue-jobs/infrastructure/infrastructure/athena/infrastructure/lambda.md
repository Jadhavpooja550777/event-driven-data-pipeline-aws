## AWS Lambda for Event-Driven ETL Trigger

Purpose:
AWS Lambda is used to trigger the AWS Glue ETL job automatically
when new data is uploaded to Amazon S3.

Trigger Source:
Amazon S3 ObjectCreated event on the input data bucket.

Functionality:
- Detect new file upload in S3 input folder
- Invoke AWS Glue ETL job programmatically
- Enable event-driven data processing

Services Integrated:
- Amazon S3 (event source)
- AWS Lambda (orchestration)
- AWS Glue (ETL processing)
- Amazon CloudWatch (logs and monitoring)

Usage in Project:
This Lambda function ensures that the ETL pipeline is triggered
automatically without manual intervention whenever new data arrives.
