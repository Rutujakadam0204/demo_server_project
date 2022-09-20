
##################***************************************     Job Portal settings     ***************************************##################

# Login URL
LOGIN_URL = '/vendor_portal/vendor-sign-up'

CELERY_BROKER_URL = 'amqp://localhost'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend'
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'http://128.0.0.1:8000/vendor_portal/vendor-sign-up'
