from .base import *

DEBUG = True
ALLOWED_HOSTS = []

 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'app_calzados',
        "USER": 'root',
        "PASSWORD": 'root',
        "PORT": '3306'
    }
}
