from .base import *

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('DB_NAME_TEST'),
        'USER': getenv('DB_USER_TEST'),
        'PASSWORD': getenv('DB_PASSWORD_TEST'),
        'PORT': getenv('DB_PORT'),
        'HOST': getenv('DB_HOST_TEST'),
    }
}
