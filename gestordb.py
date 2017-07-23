# -*- coding: utf-8 -*-

# Python's Libraries
import os
import sys
from datetime import datetime

# project_abspath = "C:\Users\Carlos\Proyectos\EstafetaConnect\src\GestorDB"
project_abspath = os.path.abspath(os.path.join(os.getcwd(), 'GestorDB'))

sys.path.append(project_abspath)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestorDB.settings")

# Django's Libraries
from django.db import connection
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Site's Models
from configuration.models import Log
from security.models import Profile
from jde.models import F0101


class ModelProfile(object):

    @classmethod
    def get(self, _user=None):

        try:
            connection.close()
            usuario = Profile.objects.all()
            return usuario

        except Exception as e:
            pass


class ModeloLog(object):

    @classmethod
    def add(self, _titulo, _texto):

        try:
            usuario = Profile.objects.get(user__username="rgonzalezz")

            log = Log()
            log.titulo = _titulo
            log.comentario = _texto
            log.created_by = usuario
            log.updated_by = usuario
            log.save()

            print "OK"
        except Exception as e:
            print str(e)


class ModeloF0101(object):

    @classmethod
    def get(self):

        direcciones = F0101.objects.all()
        return direcciones
