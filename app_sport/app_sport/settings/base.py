from pathlib import Path
from django.urls import reverse_lazy

from .local import *


import os

######################################################################################################
BASE_DIR = Path(__file__).resolve().parent.parent


######################################################################################################
SECRET_KEY = 'django-insecure-vf4_6_bple_0w0)e69_h**iqlf@4hrghk_bdy_@61r(&dk_s^k'

######################################################################################################
AUTH_USER_MODEL = 'usuarios.Usuarios'



LOGIN_URL = reverse_lazy('apps.usuarios:iniciar_sesion')
LOGIN_REDIRECT_URL = reverse_lazy('inicio')
LOGOUT_REDIRECT_URL = reverse_lazy('inicio')
######################################################################################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'apps.usuarios',
    'apps.calzados',
    'apps.opiniones',
    'apps.mensaje',

 
 


]

######################################################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
######################################################################################################
ROOT_URLCONF = 'app_sport.urls'
######################################################################################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
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

######################################################################################################
WSGI_APPLICATION = 'app_sport.wsgi.application'


######################################################################################################


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


######################################################################################################
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True

######################################################################################################


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR),'static'),)

######################################################################################################

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'media')

######################################################################################################

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

######################################################################################################