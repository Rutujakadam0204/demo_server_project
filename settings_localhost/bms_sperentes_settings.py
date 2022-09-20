
##################***************************************     Bms sperentes settings     ***************************************##################

# Login URL
LOGIN_URL = '/bms_sperentes/'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend'
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'http://128.0.0.1:8000/bms_sperentes'