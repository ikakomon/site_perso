"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from decouple import config, Csv
from django.core.wsgi import get_wsgi_application
if config('DEBUG', default=False, cast=bool)==True:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")
else : os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.prod")
application = get_wsgi_application()
