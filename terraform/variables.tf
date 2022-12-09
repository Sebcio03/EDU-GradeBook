variable "s3_bucket_name" {
  type = string
  default = "s3bucket"
}

variable "aws_access_key" {
  type = string
  default = "debug"
}

variable "aws_secret_key" {
  type = string
  default = "debug"
}

variable "aws_region" {
  type = string
  default = "eu-central-1"
}