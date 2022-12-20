from .base import *  # noqa
from .base import env


DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="ZKDdSiWGOTOABitsOQe2Xy6NINNKECHgP24s1mRu4oJTmKz1sMf1jWeeSgRM5mFl",
)
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = 1025

INSTALLED_APPS += ["debug_toolbar", "django_extensions"]  # noqa F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

CELERY_TASK_EAGER_PROPAGATES = True

AWS_S3_ENDPOINT_URL = f'http://localstack.localhost:4566/'
STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/static/"
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/media/"
