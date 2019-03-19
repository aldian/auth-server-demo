from .base import *


INSTALLED_APPS += [
    'client_app',
]


ROOT_URLCONF = 'oauth2_server_demo.urls.client_app_urls'

AUTH_SERVER_AUTHORIZE_URL = os.environ.get("AUTH_SERVER_AUTHORIZE_URL")
AUTH_SERVER_TOKEN_URL = os.environ.get("AUTH_SERVER_TOKEN_URL")

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

RESOURCE_SERVER_1_BASE_URL = os.environ.get("RESOURCE_SERVER_1_BASE_URL")
RESOURCE_SERVER_2_BASE_URL = os.environ.get("RESOURCE_SERVER_2_BASE_URL")
