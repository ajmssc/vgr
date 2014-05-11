# Django project environment-specific settings

from vgr.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

#TODO: replace localhost with the domain name of the site
DEFAULT_FROM_EMAIL = 'jsz@jsz.soumet.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'videogamereviews2',
        'USER': 'vgr',
        'PASSWORD': 'vgrpwd$#1',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


TIME_ZONE = 'America/Los_Angeles'

INTERNAL_IPS = ('127.0.0.1', )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Overwrite default ROOT_URLCONF to include static file serving by Django.
# In production, this should be handled separately by your webserver or CDN.
ROOT_URLCONF = 'vgr.urls.dev'
