"""
Django settings for accounting_system project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)lb@s#zh4gcz+65f958nc_klvhv7b=j(t6n3u260&za+=5*riw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',

    'users',
    'main',
    'hours',
    'projects',
    'reports',
    'message_box',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'accounting_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "hours/templates",
            BASE_DIR / "main/templates",
            BASE_DIR / "index/templates",
            BASE_DIR / "projects/templates/html",
            BASE_DIR / "message_box/templates/html",
        ],
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

WSGI_APPLICATION = 'accounting_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
<<<<<<< HEAD
'NAME': 'diplom',
'USER': 'niko',
'PASSWORD': '3003Nikto2004',
'HOST': 'localhost',
=======
'NAME': '',
'USER': '',
'PASSWORD': '',
'HOST': '',
>>>>>>> 42d0474 (new commit)
'PORT': ''
}
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'


STATICFILES_DIRS=(
    BASE_DIR / 'static', 
    BASE_DIR / 'media'
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 

#Users

AUTH_USER_MODEL = 'users.User'

#Logout

LOGOUT_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # This is a tuple
MEDIA_URL = '/media/'
