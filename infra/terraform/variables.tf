### AWS
## Config
# Check if LocalStack or AWS
variable "is_local" {
  type        = bool
  description = "Use LocalStack instead of AWS"
  default     = false
}
# Region
variable "region" {
  type        = string
  description = "AWS region"
}
# Access Key
variable "aws_access_key" {
  type        = string
  description = "AWS access key (LocalStack)"
}
# Secret Key
variable "aws_secret_key" {
  type        = string
  description = "AWS secret key (LocalStack)"
}

## S3
# S3 Name
variable "s3_bucket_name" {
  type        = string
  description = "S3 Bucket name"
}