# -*- coding: utf-8 -*-
import logging
import os
import sys
from datetime import timedelta
import dj_database_url

from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
server_software = os.getenv("SERVER_SOFTWARE", "")

VERSION_FILE_NAME = 'version'
VERSION_FILE_PATH = '/'.join([BASE_DIR, VERSION_FILE_NAME])

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DEBUG", False))
SERVER = os.getenv("SERVER", "local")
PRODUCTION = SERVER == "PRODUCTION"

APP_HASH = os.environ["APP_HASH"]

APP_URL = os.getenv("APP_URL", "http://127.0.0.1")

ALLOWED_HOSTS = ["*"]

SESSION_COOKIE_AGE = int(timedelta(days=365*10).total_seconds())  # 10 years

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    'channels',
    "django_rq",
)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'ROUTING': 'channels_conf.routing.channel_routing',
        'CONFIG': {
            'hosts': [os.getenv('REDIS_URL', 'redis://h:REDIS@redis:6379/0')],
        },
    },
}
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {"default": dj_database_url.config(conn_max_age=500)}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "pl"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = "/static/"
STATIC_APP_LOGO_IMG = '/static/img/app/{instance}/logo.png'
STATIC_APP_EXTERNAL_CSS = '/static/css/external/{instance}.min.css'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"

DEFAULT_SALT = str(os.environ['DEFAULT_SALT'])

LOGIN_URL = reverse_lazy("login")

SALT = str(os.environ["SALT"])

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", 'redis://localhost:6379/0'),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": sys.stdout,
        }
    },
    "loggers": {
        "django.request": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "push": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        "main": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
    },
}

INTERNAL_IPS = ("127.0.0.1",)

RQ_QUEUES = {
    "default": {
        "URL": os.getenv("REDIS_URL", 'redis://localhost:6379/0'),
        "DEFAULT_TIMEOUT": 500,
    }
}

TEST = "test" in sys.argv

APP_ENV = os.getenv("APP_ENV", "local")

ADMIN_NAME = os.getenv('ADMIN_NAME', 'Administrator')

APP_TITLE = os.getenv("APP_TITLE", "Default").decode("utf-8")
APP_NAME = os.getenv("APP_NAME", "default")
