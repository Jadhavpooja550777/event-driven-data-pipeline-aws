resource "aws_s3_bucket" "etl_bucket" {
  bucket = "myglue-etl-project"

  tags = {
    Name        = "myglue-etl-project"
    Environment = "dev"
    Project     = "event-driven-etl"
  }
}
