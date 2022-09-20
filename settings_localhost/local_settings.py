# For django-environ to read the .env file
# import environ
# env = environ.Env()
# environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE'	: 'django.db.backends.postgresql_psycopg2',
        'NAME'		: 'demo_project',
        'USER'		: 'postgres',
        'PASSWORD'	: 'postgres',
        'HOST'		: 'localhost',
        'PORT'		: '5432',
        #'ENGINE'        : 'django.db.backends.postgresql_psycopg2',
        #'NAME'          : env("DEFAULT_DATABASE_NAME"),
        #'USER'          : env("DEFAULT_DATABASE_USER"),
        #'PASSWORD'      : env("DEFAULT_DATABASE_PASSWORD"),
        #'HOST'          : env("DEFAULT_DATABASE_HOST"),
        #'PORT'          : env("DEFAULT_DATABASE_PORT"),
    },

    'log': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'log',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },

    'community': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'community', 
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },

    'log_community': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'community_log',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },

    'bms_sperentes': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bms_sperentes',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },

    'bms_sperentes_log': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'bms_sperentes_log',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },

    'vendor_portal': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vendor_portal', 
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },

    'vendor_portal_log': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'vendor_portal_log',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

'''
# Server DB
'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bms_ssl',
        'USER': 'djangodeveloper',
        'PASSWORD': 'Django@1234',
        'HOST': '192.168.0.100',
        'PORT': '5432',
    },   
'''

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASE_ROUTERS = ['apps.applicant.router.CheckerRouter']  # it consists the path where your router.py file reside. in my case it is in contenter app.
