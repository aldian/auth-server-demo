from .base import *


ALLOWED_HOSTS = ['localhost', 'auth-server.test']


INSTALLED_APPS += [
    'oauth2_provider',
]


ROOT_URLCONF = 'oauth2_server_demo.urls.auth_server_urls'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': os.environ.get('DB_USER'),
        'HOST': os.environ.get('DB_HOST'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'PORT': 5432,
    }
}


OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'introspection': 'Introspection scope',
    },

    'DEFAULT_SCOPES': ['read', 'introspection'],
}