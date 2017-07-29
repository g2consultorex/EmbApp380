# -*- coding: utf-8 -*-

# Python's Libraries
import os
import sys

# project_abspath = "C:\Users\Carlos\Proyectos\EstafetaConnect\src\GestorDB"
project_abspath = os.path.abspath(os.path.join(os.getcwd(), 'CapaDatos'))

sys.path.append(project_abspath)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestorDB.settings")

# Django's Libraries
from django.db import connection
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Site's Models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from configuration.models import EstafetaUser
from jde.models import F0101
from jde.models import F4211
from jde.models import F42119
from jde.models import F41001
from jde.models import F0116
from jde.models import F0005
from jde.models import F0115
# from jde.models import F01151
from jde.models import F0111


class ModeloUsuario(object):

    @classmethod
    def login(self, _username, _password):

        try:
            usuario = authenticate(username=_username, password=_password)

            if usuario:
                return usuario.is_active
            else:
                return False

        except Exception as e:
            print str(e)

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
    def edit(self, _username, _first_name, _last_name, _password, _active):

        try:

            usuario = User.objects.get(username=_username)
            usuario.first_name = _first_name
            usuario.last_name = _last_name
            usuario.is_active = _active

            if _password != '':
                usuario.set_password(_password)

            usuario.save()

        except Exception as e:
            print str(e)


class ModeloEstafetaUser(object):

    @classmethod
    def get(self):

        try:
            connection.close()
            records = EstafetaUser.objects.all().order_by('created_date')
            return records

        except Exception:
            pass

    @classmethod
    def add(self, _clave, _url, _login, _password, _quadrant, _suscriber_id, _paper_type, _es_principal, _customer_number):

        try:
            estafeta = EstafetaUser()

            estafeta.clave = _clave
            estafeta.url = _url
            estafeta.login = _login
            estafeta.password = _password
            estafeta.quadrant = _quadrant
            estafeta.suscriber_id = _suscriber_id
            estafeta.paper_type = _paper_type
            estafeta.es_principal = _es_principal
            estafeta.customer_number = _customer_number

            estafeta.save()

        except Exception as e:
            print str(e)

    @classmethod
    def edit(self, _clave, _url, _login, _password, _quadrant, _suscriber_id, _paper_type, _es_principal, _customer_number):

        try:

            estafeta = EstafetaUser.objects.get(clave=_clave)
            estafeta.login = _login
            estafeta.url = _url
            estafeta.password = _password
            estafeta.quadrant = _quadrant
            estafeta.suscriber_id = _suscriber_id
            estafeta.paper_type = _paper_type
            estafeta.es_principal = _es_principal
            estafeta.customer_number = _customer_number

            estafeta.save()

        except Exception as e:
            print str(e)


class Factura(object):

    @classmethod
    def get(self, _numero, _tipo):

        try:
            factura = F4211.objects.using('jde').filter(
                SDDOC=_numero,
                SDDCT=_tipo
            )

            if len(factura) == 0:
                factura = F42119.objects.using('jde').filter(
                    SDDOC=_numero,
                    SDDCT=_tipo
                )

            return factura

        except Exception as error:
            value = {
                'mensaje': str(error)
            }
            return False, value


class DireccionOrigen(object):

    @classmethod
    def get(self, _numero, _tipo):

        datos = {}
        datos['corporatename'] = ""
        datos['address1'] = ""
        datos['address2'] = ""
        datos['cellphone'] = ""
        datos['city'] = ""
        datos['contactname'] = ""
        datos['customernumber'] = ""
        datos['neighborhood'] = ""
        datos['phonenumber'] = ""
        datos['zipcode'] = ""
        datos['state'] = ""

        try:
            factura = F4211.objects.using('jde').filter(
                SDDOC=_numero,
                SDDCT=_tipo
            )

            if len(factura) == 0:
                factura = F42119.objects.using('jde').filter(
                    SDDOC=_numero,
                    SDDCT=_tipo
                )

            almacen = F41001.objects.using('jde').filter(
                CIMCU__contains=factura[0].SDMCU
            )

            direccion = F0101.objects.using('jde').filter(
                ABAN8=almacen[0].CIAN8
            )

            dir_complemento = F0116.objects.using('jde').filter(
                ALAN8=almacen[0].CIAN8
            )

            direccion_Tel = F0115.objects.using('jde').filter(
                WPAN8=almacen[0].CIAN8
            )

            direccion_Cel = F0115.objects.using('jde').filter(
                WPAN8=almacen[0].CIAN8,
                WPPHTP__contains='CAR'
            )

            direccion_Resp = F0111.objects.using('jde').filter(
                WWAN8=almacen[0].CIAN8
            )

            UDCestado = F0005.objects.using('jde').filter(
                DRSY__contains='00',
                DRRT__contains='S',
                DRKY__contains=dir_complemento[0].ALADDS
            )

            if len(factura) > 0:

                if len(dir_complemento) > 0:
                    datos['corporatename'] = "%s %s" % (
                        direccion[0].ABALPH,
                        dir_complemento[0].ALADD1
                    )
                    datos["address1"] = dir_complemento[0].ALADD2
                    datos["address2"] = dir_complemento[0].ALADD3
                    datos['city'] = dir_complemento[0].ALCTY1
                    # datos['customernumber'] = dir_complemento[0] <-- Usuario Estafeta
                    datos['neighborhood'] = dir_complemento[0].ALADD4
                    datos['zipcode'] = dir_complemento[0].ALADDZ

                    if len(UDCestado) > 0:
                        datos['state'] = "%s" % (UDCestado[0].DRDL01)

                    if len(direccion_Tel) > 0:
                        datos['phonenumber'] = "%s %s" % (
                            direccion_Tel[0].WPAR1,
                            direccion_Tel[0].WPPH1
                        )
                    if len(direccion_Resp) > 0:
                        datos['contactname'] = direccion_Resp[0].WWALPH

                    if len(direccion_Cel) > 0:
                        datos['cellphone'] = "%s %s" % (
                            direccion_Cel[0].WPAR1,
                            direccion_Cel[0].WPPH1
                        )

            return True, datos

        except Exception as error:
            value = {
                'mensaje': str(error)
            }
            return False, value


class DireccionDestino(object):

    @classmethod
    def get(self, _numero, _tipo):

        datos = {}
        datos['corporatename'] = ""
        datos['address1'] = ""
        datos['address2'] = ""
        datos['cellphone'] = ""
        datos['city'] = ""
        datos['contactname'] = ""
        datos['customernumber'] = ""
        datos['neighborhood'] = ""
        datos['phonenumber'] = ""
        datos['zipcode'] = ""
        datos['state'] = ""
        datos['Country'] = ""

        try:
            factura = F4211.objects.using('jde').filter(
                SDDOC=_numero,
                SDDCT=_tipo
            )

            if len(factura) == 0:
                factura = F42119.objects.using('jde').filter(
                    SDDOC=_numero,
                    SDDCT=_tipo
                )

            direccionDest = F0101.objects.using('jde').filter(
                ABAN8=factura[0].SDSHAN
            )

            dir_complementoDestino = F0116.objects.using('jde').filter(
                ALAN8=factura[0].SDSHAN
            )

            direccionDest_Tel = F0115.objects.using('jde').filter(
                WPAN8=factura[0].SDSHAN
            )

            direccionDest_Cel = F0115.objects.using('jde').filter(
                WPAN8=factura[0].SDSHAN,
                WPPHTP__contains='CAR'
            )

            # direccionDest_Correo = F01151.objects.using('jde').filter(
            #     EAAN8=factura[0].SDSHAN,
            #     EAETP__contains='E',
            #     EAEHIER=0,
            #     EAECLASS__contains='ASN'
            # )

            direccionDest_Resp = F0111.objects.using('jde').filter(
                WWAN8=factura[0].SDSHAN
            )

            UDCestadoDest = F0005.objects.using('jde').filter(
                DRSY__contains='00',
                DRRT__contains='S',
                DRKY__contains=dir_complementoDestino[0].ALADDS
            )

            if len(factura) > 0:

                datos['customernumber'] = str(factura[0].SDSHAN)

                if len(dir_complementoDestino) > 0:
                    datos['corporatename'] = "%s %s" % (
                        direccionDest[0].ABALPH.strip(),
                        dir_complementoDestino[0].ALADD1.strip()
                    )
                    datos["address1"] = dir_complementoDestino[0].ALADD2
                    datos["address2"] = dir_complementoDestino[0].ALADD3
                    datos['city'] = dir_complementoDestino[0].ALCTY1
                    datos['neighborhood'] = dir_complementoDestino[0].ALADD4
                    datos['zipcode'] = dir_complementoDestino[0].ALADDZ
                    datos['Country'] = dir_complementoDestino[0].ALCTR

                    if len(UDCestadoDest) > 0:
                        datos['state'] = "%s" % (UDCestadoDest[0].DRDL01)

                    if len(direccionDest_Tel) > 0:
                        datos['phonenumber'] = "%s %s" % (
                            direccionDest_Tel[0].WPAR1,
                            direccionDest_Tel[0].WPPH1
                        )

                    if len(direccionDest_Resp) > 0:
                        datos['contactname'] = direccionDest_Resp[0].WWALPH

                    if len(direccionDest_Cel) > 0:
                        datos['cellphone'] = "%s %s" % (
                            direccionDest_Cel[0].WPAR1,
                            direccionDest_Cel[0].WPPH1
                        )

            return True, datos

        except Exception as error:
            value = {
                'mensaje': str(error)
            }
            return False, value
