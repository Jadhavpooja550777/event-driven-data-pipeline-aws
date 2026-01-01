resource "aws_glue_job" "etl_job" {
  name     = "my-glue-etl-job"
  role_arn = aws_iam_role.glue_service_role.arn

  command {
    name            = "glueetl"
    script_location = "s3://myglue-etl-project/scripts/etl_job.py"
    python_version  = "3"
  }
}
