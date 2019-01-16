"""
WSGI config for BridgeMaster project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import django
import sys
from django.core.wsgi import get_wsgi_application

path='/home/pi/project/BridgeMaster'
if path not in sys.path:
    sys.path.append(path)

application = django.core.handlers.wsgi.WSGIHandler()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BridgeMaster.settings")
application = django.core.handlers.wsgi.WSGIHandler()
