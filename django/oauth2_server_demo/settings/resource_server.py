from .base import *


INSTALLED_APPS += [
    'rest_framework',
    'resource_server',
]

ROOT_URLCONF = 'oauth2_server_demo.urls.resource_server_urls'

AUTH_SERVER_INTROSPECTION_URL = os.environ.get("AUTH_SERVER_INTROSPECTION_URL")
