from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ElectroLac',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {
        'min_length': 12}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
      
    "/Users/lcolo/Desktop/P_Final_Proyectos/ElectroLac/static",
    "C:\ProyectoFinal\ElectroLac\ElectroLac\static",
 
]
CRISPY_TEMPLATE_PACK='bootstrap4'
LOGIN_REDIRECT_URL = 'account'

LOGOUT_REDIRECT_URL = 'login'

MEDIA_URL = '/media/'

import os

MEDIA_ROOT = '/Users/lcolo/Desktop/P_Final_Proyectos/ElectroLac/media'
