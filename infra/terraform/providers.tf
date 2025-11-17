provider "aws" {
  region     = var.region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key

  skip_credentials_validation = var.is_local
  skip_metadata_api_check     = var.is_local
  skip_requesting_account_id  = var.is_local
  s3_use_path_style           = var.is_local

  endpoints {
    s3 = var.is_local ? "http://localhost:4566" : null
  }
}
