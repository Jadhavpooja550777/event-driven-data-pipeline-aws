import json
import boto3

# Create a Glue client using boto3

glue = boto3.client('glue')

# This is the main Lambda function
# AWS Lambda always starts execution from this function
def lambda_handler(event, context):

    # Start the AWS Glue ETL job using its job name
    # This tells Glue to begin processing the newly uploaded data
    response = glue.start_job_run(
        JobName='my-glue-etl-job'
    )

   
    # statusCode 200 indicates successful execution
 
    return {
        'statusCode': 200,
        'body': json.dumps('Glue job triggered successfully')
    }
