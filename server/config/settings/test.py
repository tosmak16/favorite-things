from .base import *

DEBUG = False

SECRET_KEY = 'secret'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('DB_NAME_TEST'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
        'PORT': getenv('DB_PORT'),
        'HOST': getenv('DB_HOST'),
    }
}
