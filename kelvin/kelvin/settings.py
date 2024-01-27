"""
Django settings for kelvin project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# CONCERT SETTINGS #######

CONCERT_STATUS = "forsale"  # upcoming, over, soldout, forsale, notyet # are the options *case sensitive*

CONCERT_LIST = [
    {
        "soldOut": False,
        "date": "18th November 2023",
        "tickets": [
            {
                "ticketLabel": "Standard Ticket",
                "ticketID": "price_1OFVVXDysBLU7VPvWnC7jH1Z",
            },
            {
                "ticketLabel": "Concession Ticket",
                "ticketID": "price_1OFVVXDysBLU7VPvJhWYmQ1D",
            },
            {
                "ticketLabel": "Restricted View Ticket",
                "ticketID": "price_1OFhKCDysBLU7VPvXpb95h3Q",
            },
        ],
    }
]

# CONCERT SETTINGS END HERE DO NOT CHANGE ANYTHING BELOW UNLESS CONFIDENT ######

import os, sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


from dotenv import load_dotenv

dotenv_file = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_file)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]
STRIPE_SECRET_KEY = os.environ["STRIPE_SECRET_KEY"]
STRIPE_PUBLIC_SECRET = os.environ["STRIPE_PUBLIC_SECRET"]
# STRIPE_ENDPOINT_SECRET = os.environ['STRIPE_ENDPOINT_SECRET']

STRIPE_ENDPOINT_SECRET = (
    "whsec_7390c4a8a79fc04e2a50f24b2fdd39809814f7e8686a0c74306d0a6a38095320"
)

TICKETS_PASSWORD = os.environ["tickets_password"]

COOKIE_DATA = {}

# STRIPE SETTINGS ######
# REDIRECT_DOMAIN = 'http://yukisuter.pythonanywhere.com'
REDIRECT_DOMAIN = "http://127.0.0.1:8000"


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", ".kelvin-ensemble.co.uk", "yukisuter.pythonanywhere.com"]


# Application definition

INSTALLED_APPS = [
    "kelvin",
    "website",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "kelvin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
            ],
        },
    },
]

SETTINGS_EXPORT = [
    "CONCERT_STATUS",
    "CONCERT_LIST",
    "STRIPE_SECRET_KEY",
    "REDIRECT_DOMAIN",
]


WSGI_APPLICATION = "kelvin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# STATICFILES_DIRS = [
#     os.path.join(PROJECT_DIR, 'static')
# ]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
