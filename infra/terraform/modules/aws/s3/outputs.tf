# S3 Bucket
output "s3_bucket" {
  description = "S3 Bucket"
  value       = aws_s3_bucket.this.bucket
}