## AWS Glue ETL Job

Purpose:
AWS Glue is used to process raw data stored in Amazon S3 and generate
cleaned and transformed data for analytics.

Input Data Location:
s3://myglue-etl-project/input/

Output Data Location:
s3://myglue-etl-project/output/

Processing Logic:
- Read raw CSV data from S3
- Perform basic data cleaning and transformation
- Write processed data back to S3 in a structured format

Trigger Mechanism:
The ETL job is triggered in an event-driven manner when new data
is uploaded to the S3 input location.

IAM Role:
The Glue job uses a dedicated IAM service role to access S3 and CloudWatch.
