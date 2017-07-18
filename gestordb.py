# -*- coding: utf-8 -*-

# Python's Libraries
import os
import sys
from datetime import datetime

#import ipdb; ipdb.set_trace()

project_abspath = "C:\Users\Carlos\Proyectos\EstafetaConnect\src\GestorDB"

sys.path.append(project_abspath)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestorDB.settings")

# Django's Libraries
from django.db import connection
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Site's Models
from configuration.models import Log
from security.models import	Profile	

class ModeloLog(object):

    @classmethod
    def add(self, _titulo, _texto):

    	try:
    		usuario = Profile.objects.get(user__username = "rgonzalezz")

    		log = Log()
    		log.titulo = _titulo
    		log.comentario = _texto
    		log.created_by= usuario	
    		log.updated_by = usuario	
    		log.save()

    		print "OK"	
    	except Exception as e:
    		print str(e)

