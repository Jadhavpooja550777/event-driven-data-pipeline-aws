import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality


# ---------------------------------------------------
# Initialize Glue job and Spark context
# ---------------------------------------------------
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# ---------------------------------------------------
# Define data quality rules
# ---------------------------------------------------
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""


# ---------------------------------------------------
# Read source data from S3 using Glue Data Catalog
# ---------------------------------------------------
source_df = glueContext.create_dynamic_frame.from_catalog(
    database="mydatabase",
    table_name="product"
)


# ---------------------------------------------------
# Apply data quality validation rules
# ---------------------------------------------------
EvaluateDataQuality().process_rows(
    frame=source_df,
    ruleset=DEFAULT_DATA_QUALITY_RULESET,
    publishing_options={
        "dataQualityEvaluationContext": "EvaluateDataQuality",
        "enableDataQualityResultsPublishing": True
    },
    additional_options={
        "dataQualityResultsPublishing.strategy": "BEST_EFFORT",
        "observations.scope": "ALL"
    }
)


# ---------------------------------------------------
# Write processed data to S3 in Parquet format
# ---------------------------------------------------
glueContext.write_dynamic_frame.from_options(
    frame=source_df,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://myglue-etl-project/output/",
        "partitionKeys": []
    },
    format_options={
        "compression": "snappy"
    }
)


# ---------------------------------------------------
# Commit Glue job
# ---------------------------------------------------
job.commit()
