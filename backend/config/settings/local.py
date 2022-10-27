from .base import *  # noqa
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="ZKDdSiWGOTOABitsOQe2Xy6NINNKECHgP24s1mRu4oJTmKz1sMf1jWeeSgRM5mFl",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ['localhost:5173', '0.0.0.0:5173', '127.0.0.1:5173']

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
INTERNAL_IPS = ["127.0.0.1"]

CELERY_TASK_EAGER_PROPAGATES = True
