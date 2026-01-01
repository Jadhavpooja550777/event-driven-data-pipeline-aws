# Glue ETL script for event-driven data pipeline
# Reads raw data from S3 input folder
# Writes processed data to S3 output folder


import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1767169381964 = glueContext.create_dynamic_frame.from_catalog(database="mydatabase", table_name="product", transformation_ctx="AmazonS3_node1767169381964")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=AmazonS3_node1767169381964, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1767169321932", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1767169388293 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3_node1767169381964, connection_type="s3", format="glueparquet", connection_options={"path": "s3://myglue-etl-project/output/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1767169388293")

job.commit()
