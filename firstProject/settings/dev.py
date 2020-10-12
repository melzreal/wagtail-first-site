from .base import *
import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/btre')
load_dotenv(os.path.join(project_folder, '.env'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wd@%w4e_q^1jh!(+u=k9e^e6jrst$n0!bx8w6tq0hhq748&*6n'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = ("127.0.0.1, 172.17.0.1")

try:
    from .local import *
except ImportError:
    pass
