from .common import *

DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
)

ALLOWED_HOSTS = [
    'localhost',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jtx_test',
        'USER': 'root',
        'PASSWORD': '',
    }
}

