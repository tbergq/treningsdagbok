# -*- coding: utf-8 -*-
"""
WSGI config for treningsdagbok project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys
path = 'home/tbergq/treningsdagbok/'
if path not in sys.path:
    sys.path.append(path)
os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treningsdagbok.settings")

import django
django.setup()

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()