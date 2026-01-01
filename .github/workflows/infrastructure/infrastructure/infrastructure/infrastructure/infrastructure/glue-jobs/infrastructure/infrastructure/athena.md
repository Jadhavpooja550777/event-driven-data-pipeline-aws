## Amazon Athena for Analytics and Reporting

Purpose:
Amazon Athena is used to analyze processed data stored in Amazon S3
without managing any servers.

Data Source:
Processed data stored at:
s3://myglue-etl-project/output/

Table Metadata:
Tables are created using AWS Glue Data Catalog, allowing Athena to
query the data using standard SQL.

Usage in Project:
Athena is used to generate summary insights from the processed data,
which can be scheduled for daily reporting.

Query Results Location:
s3://myglue-etl-project/athena-results/
