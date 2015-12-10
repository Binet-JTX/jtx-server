from .common import *

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = True

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'django_extensions',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
