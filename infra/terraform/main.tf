### Main
## AWS
# S3
module "s3" {
  source         = "./modules/aws/s3"
  s3_bucket_name = var.s3_bucket_name
}