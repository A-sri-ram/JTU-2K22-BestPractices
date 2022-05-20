"""
Django settings for cjapp project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from typing import Dict, List, Union

import environ

env: environ.Env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR : str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY : str = env('secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG : bool = bool(os.getenv("DEBUG", 'False').lower() in ('true', '1', 't','True'))

# Application definition

INSTALLED_APPS : list[str] = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'restapi'
]

MIDDLEWARE : list[str] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'restapi.disable_csrf.DisableCSRF',

]

# We could static type below variable as : Dict[str, x ], if we are sure about what data types that x can take (using Union)
# Lets say x could be Union[str, List[str], int]

REST_FRAMEWORK  = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
DEFAULT_PORT = env('DEFAULT_PORT')
ROOT_URLCONF = 'cjapp.urls'

# We could static type below variable as : List[Dict[str, x ]], if we are sure about what data types that x can take (using Union)
# Lets say x could be Union[str, List[str], int, bool, Dict[str, List[str]]]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# We could static type below variable as : Dict[str, x ], if we are sure about what data types that x can take (using Union)
# Lets say x could be Union[str, List[str], int, bool, Dict[str, Dict[str, str]]]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'level': 'DEBUG',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['file'],
        },
    },
    'formatters': {
        'verbose': {
            'format': '{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },

}

WSGI_APPLICATION : str = 'cjapp.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES: Dict[str, dict[str: str]] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS : List[Dict[str, str]] = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE:str = env('LANGUAGE_CODE')

TIME_ZONE : str = 'UTC'

USE_I18N : bool = True

USE_L10N : bool = True

USE_TZ : bool = True

ALLOWED_HOSTS : List[str] = ['*']

CORS_ORIGIN_ALLOW_ALL : bool = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL:str = '/static/'
