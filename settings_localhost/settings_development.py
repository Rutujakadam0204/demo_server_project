"""
Django settings for bms project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import sys
import datetime

from pathlib import Path
from django.contrib.messages import constants as messages
from django.conf import settings
from . import community_settings, job_portal_settings, vendor_portal_settings

# For django-environ to read the .env file
import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# Import Database Settings
try:
    from bms.local_settings import *
except ImportError:
    pass


# Application definition
CUSTOM_APPS = [
    'apps.login',
    'apps.widget',
    'apps.contact_mgmt',
    'apps.sales',
    'apps.marketing',
    'apps.customer_service',
    'apps.project_mgmt_advance',
    'apps.project_mgmt_basic',
    'apps.global_settings',
    'apps.hrms',
    'apps.document',
    'apps.training',
    'apps.assets',
    'apps.feedback',
    'apps.vendor_management',
    'apps.inventory_management',
    'apps.select_settings',
    'apps.market_research',
    'apps.compliance',
    'apps.accounting',
    'apps.organization',
    'apps.report_slick',
    'apps.analytics',
    'apps.settings',
    'apps.log',
    'apps.ticket',
    'apps.product',
    'apps.report',
    'apps.license_management',
    'apps.idea',
    'apps.notification',
    'apps.bms_geo_location',
    'apps.user_company_profile',

    # community app
    'community.apps.chat',
    'community.apps.community_geo_location',
    'community.apps.company',
    'community.apps.company_settings',
    'community.apps.feedback',
    'community.apps.groups',
    'community.apps.invitation',
    'community.apps.job',
    'community.apps.log_community',
    'community.apps.my_profile',
    'community.apps.page',
    'community.apps.ticket',
    'community.apps.user_settings',
    'storages',
    'notifications',
    
    

    # Job Portal
    'job_portal.apps.bms_geo_location',
    'job_portal.apps.applicant',
    'job_portal.apps.job_description',
    'job_portal.apps.log_job_portal',
    'job_portal.apps.feedback',
    'job_portal.apps.ticket',

    # license portal
    'license_portal.apps.license_management',

    # customer portal
    'customer_portal.apps.login',
    'customer_portal.apps.ticket',
    'customer_portal.apps.accounting',
    'customer_portal.apps.bms_geo_location',
    'customer_portal.apps.feedback',

    # sperentes admin
    'sperentes_admin.apps.bms',
    'sperentes_admin.apps.product',
    'sperentes_admin.apps.login',
    'sperentes_admin.apps.sperentes_admin_log',

    # vendor portal
    'vendor_portal.apps.bms_geo_location',
    'vendor_portal.apps.feedback',
    'vendor_portal.apps.inventory_management',
    'vendor_portal.apps.log_vendor',
    'vendor_portal.apps.report_slick',
    'vendor_portal.apps.select_settings',
    'vendor_portal.apps.settings',
    # 'vendor_portal.apps.slick_reporting',
    'vendor_portal.apps.ticket',
    'vendor_portal.apps.vendor_login',
    'vendor_portal.apps.widget',

    # video_call
    'video_conference.apps.video_call',
    'video_conference.apps.log_video_calling',

    # bms sperentes
    'bms_sperentes.apps1.login',
    'bms_sperentes.apps1.widget',
    'bms_sperentes.apps1.contact_mgmt',
    'bms_sperentes.apps1.sales',
    'bms_sperentes.apps1.marketing',
    'bms_sperentes.apps1.customer_service',
    'bms_sperentes.apps1.project_mgmt_advance',
    'bms_sperentes.apps1.project_mgmt_basic',
    'bms_sperentes.apps1.global_settings',
    'bms_sperentes.apps1.hrms',
    'bms_sperentes.apps1.document',
    'bms_sperentes.apps1.training',
    'bms_sperentes.apps1.assets',
    'bms_sperentes.apps1.feedback_incoming',
    'bms_sperentes.apps1.feedback_internal',
    'bms_sperentes.apps1.vendor_management',
    'bms_sperentes.apps1.inventory_management',
    'bms_sperentes.apps1.select_settings',
    'bms_sperentes.apps1.market_research',
    'bms_sperentes.apps1.compliance',
    'bms_sperentes.apps1.accounting',
    'bms_sperentes.apps1.organization',
    'bms_sperentes.apps1.report_slick',
    'bms_sperentes.apps1.analytics',
    'bms_sperentes.apps1.settings',
    'bms_sperentes.apps1.log',
    'bms_sperentes.apps1.ticket',
    'bms_sperentes.apps1.ticket_incoming',
    'bms_sperentes.apps1.product',
    'bms_sperentes.apps1.report',
    'bms_sperentes.apps1.license_management',
    'bms_sperentes.apps1.idea',
    'bms_sperentes.apps1.notification',
    'bms_sperentes.apps1.bms_geo_location',
    'bms_sperentes.apps1.bug_tracker',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'channels',
    'slick_reporting'
]

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
]

INSTALLED_APPS = CUSTOM_APPS + THIRD_PARTY_APPS + DEFAULT_APPS

# Point Django To Apps Folder
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.user_company_profile.get_username.RequestMiddleware'
]

ROOT_URLCONF = 'bms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.login.context_processors.profile_form',
                'apps.login.context_processors.community_permission',
                'apps.widget.context_processors.email_credential_form',
                'apps.widget.context_processors.meeting_form',
                'apps.widget.context_processors.reminder_form',
                'apps.widget.context_processors.task_form',
                'apps.widget.context_processors.note_form',
                'apps.widget.context_processors.group_form',
                'apps.widget.context_processors.employee_feedback',
                'apps.widget.context_processors.sperenets_feedback',
                'apps.widget.context_processors.my_message',

                # community
                # 'community.apps.my_profile.context_processor.user_form',
            ],
        },
    },
]

WSGI_APPLICATION = 'bms.wsgi.application'
ASGI_APPLICATION = 'bms.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE	= 'en-us'
TIME_ZONE		= 'Asia/Kolkata'
USE_I18N		= True
USE_L10N		= True
USE_TZ			= True

# AWS S3 Storage for Static & Media files
AWS_ACCESS_KEY_ID       = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY   = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN    = env("AWS_S3_CUSTOM_DOMAIN")
DEFAULT_FILE_STORAGE    = env("DEFAULT_FILE_STORAGE")
AWS_LOCATION            = env("AWS_LOCATION")
STATICFILES_STORAGE     = env("STATICFILES_STORAGE")
STATIC_URL              = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Login URL
LOGIN_URL = '/'

# Email Settings
EMAIL_BACKEND           = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS           = True
EMAIL_HOST              = env("EMAIL_HOST")
EMAIL_PORT              = env("EMAIL_PORT")
EMAIL_HOST_USER         = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD     = env("EMAIL_HOST_PASSWORD")

# Celery
CELERY_BROKER_URL = 'amqp://localhost'
# CELERY_BROKER_URL	= env("CELERY_BROKER_URL")

# CK Editor Settings
CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media/uploads/')
CKEDITOR_CONFIGS = {
    'default': {

        'toolbar': [['Cut', 'Copy', 'Paste'],

                    ['Bold', 'Italic', 'Underline', 'Strike'],
                    ['NumberedList', 'BulletedList', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
                     '-', 'TextColor', 'BGColor'],
                    ['Styles', 'Format', 'Font', 'FontSize']
                    ],
        'height': 190,
        'width': '100%',
    }

}

# Django Messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SLICK_REPORTING_DEFAULT_START_DATE = datetime.datetime.now()
SLICK_REPORTING_DEFAULT_END_DATE = datetime.datetime.now()
SLICK_REPORTING_FORM_MEDIA = {

    'css': {
        'all': (
            'https://cdn.datatables.net/v/bs4/dt-1.10.20/datatables.min.css',
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.css',
        )
    },
    'js': (
        'https://code.jquery.com/jquery-3.3.1.slim.min.js',
        'https://cdn.datatables.net/v/bs4/dt-1.10.20/datatables.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js',
        'https://code.highcharts.com/highcharts.js',
    )
}

# SLICK_REPORTING_FORM_MEDIA = getattr(settings, 'SLICK_REPORTING_FORM_MEDIA', SLICK_REPORTING_FORM_MEDIA_DEFAULT)
SLICK_REPORTING_DEFAULT_CHARTS_ENGINE = getattr(settings, 'SLICK_REPORTING_DEFAULT_CHARTS_ENGINE', 'highcharts')

DATABASE_ROUTERS = ('apps.db_routers.DbRouter',)

RAZOR_KEY_ID            = env("RAZOR_KEY_ID")
RAZOR_KEY_SECRET        = env("RAZOR_KEY_SECRET")

SITE_ID = 1
