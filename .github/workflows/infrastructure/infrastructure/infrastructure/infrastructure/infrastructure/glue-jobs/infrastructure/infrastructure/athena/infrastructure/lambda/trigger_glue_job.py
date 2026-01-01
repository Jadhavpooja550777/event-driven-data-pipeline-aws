import json
import boto3

glue = boto3.client('glue')

def lambda_handler(event, context):
    """
    Triggered when a file is uploaded to S3.
    Starts the AWS Glue ETL job.
    """

    response = glue.start_job_run(
        JobName='my-glue-etl-job'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Glue job triggered successfully')
    }
