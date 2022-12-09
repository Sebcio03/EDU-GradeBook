# EDU
#### OpenSource Online GradeBook

# Purpose
- Learn Vue/Nuxt (with Vuex)
- Master Django

# Stack
* Backend
    * Aiohttp (TODO)
    * Django/Django Rest Framework
    * Django Channels (TODO)
    * PostgreSQL
    * Celery
    * RabbitMQ (TODO)
    * Redis
    * PyTest
* Frontend
    * Vue3/Vuex
    * Nuxt (TODO)
    * TailwindCSS (with PostCSS)
    * Jest (TODO)
* Tools 
    * Docker
    * Kubernetes (TODO)
    * Terraform
    * LocalStack
* Testing
    * Selenium (TODO)
* Third-Party Tools 
    * Amazon Web Services
    * Circle CI (TODO)
    * Sentry
    * DataDog (TODO)

# Set up the project  

## Environment variables 

Envs are stored in .env directory
- Dev environments are in .local/.<service_name> 
- Prod environments are in .env/.production/.<service_name>
- Example environments are in .env/example/.<service_name>

## Terraform (AWS)

> With localstack use [terraform-local](https://pypi.org/project/terraform-local/)

terraform.tfvars
```tfvars
s3_bucket_name = "s3bucket"
aws_access_key = "default"
aws_secret_key = "default"
aws_region = "eu-central-1"
```

## Migrations

```bash
docker exec -it {local/production}_django python manage.py makemigrations
docker exec -it {local/production}_django python manage.py migrate
```