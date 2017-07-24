# -*- coding: utf-8 -*-

# Python's Libraries
import os
import sys

# project_abspath = "C:\Users\Carlos\Proyectos\EstafetaConnect\src\GestorDB"
project_abspath = os.path.abspath(os.path.join(os.getcwd(), 'GestorDB'))

sys.path.append(project_abspath)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestorDB.settings")

# Django's Libraries
from django.db import connection
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Site's Models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from configuration.models import Log
from security.models import Profile
from jde.models import F0101
from jde.models import F4211
from jde.models import F42119
from jde.models import F41001
from jde.models import F0116


class ModeloUsuario(object):

    @classmethod
    def get(self, _user=None):

        try:
            connection.close()
            usuario = User.objects.all().order_by('date_joined')
            return usuario

        except Exception:
            pass

    @classmethod
    def add(self, _username, _first_name, _last_name, _password):

        try:

            usuario = User()
            usuario.username = _username
            usuario.first_name = _first_name
            usuario.last_name = _last_name
            if _password != '':
                usuario.set_password(_password)
            else:
                usuario.set_password("12345")
            usuario.save()

        except Exception as e:
            print str(e)

    @classmethod
    def edit(self, _username, _first_name, _last_name, _password):

        try:

            usuario = User.objects.get(username=_username)
            usuario.first_name = _first_name
            usuario.last_name = _last_name

            if _password != '':
                usuario.set_password(_password)

            usuario.save()

        except Exception as e:
            print str(e)

    @classmethod
    def login(self, _username, _password):

        try:
            usuario = authenticate(username=_username, password=_password)

            if usuario:
                return True
            else:
                return False

        except Exception as e:
            print str(e)


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


class Factura(object):

    @classmethod
    def get(self, _numero, _tipo):

        try:
            factura = F4211.objects.using('jde').filter(
                SDDOC=_numero, SDDCT=_tipo)

            if len(factura) == 0:
                factura = F42119.objects.using(
                    'jde').filter(SDDOC=_numero, SDDCT=_tipo)

            print factura

        except Exception as e:
            print str(e)


class DireccionOrigen(object):

    @classmethod
    def get(self, _numero, _tipo):

        try:
            factura = F4211.objects.using('jde').filter(
                SDDOC=_numero, SDDCT=_tipo)

            if len(factura) == 0:
                factura = F42119.objects.using(
                    'jde').filter(SDDOC=_numero, SDDCT=_tipo)

            almacen = F41001.objects.using('jde').filter(
                CIMCU__contains=factura[0].SDMCU)

            direccion = F0101.objects.using(
                'jde').filter(ABAN8=almacen[0].CIAN8)

            direccion_complemento = F0116.objects.using(
                'jde').filter(ALAN8=almacen[0].CIAN8)

            return direccion, direccion_complemento

        except Exception as e:
            print str(e)
