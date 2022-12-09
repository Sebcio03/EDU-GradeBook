resource "aws_s3_bucket" "django_data" {
  bucket = var.s3_bucket_name
  tags = {
    Name        = "django_data"
  }
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.django_data.id
  acl    = "public-read"
}