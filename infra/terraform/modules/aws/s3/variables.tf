# S3 Name
variable "s3_bucket_name" {
  type = string
}

# S3 Tags
variable "tags" {
  description = "S3 Tags"
  type        = map(string)
  default     = {}
}