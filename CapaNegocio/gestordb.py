# -*- coding: utf-8 -*-

# Python's Libraries
import os
import sys
import time
import datetime

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
from django.db.models import Q

from configuration.models import EstafetaAmbiente
# from security.models import Profile
from jde.models import F0101
from jde.models import F4211
from jde.models import F42119
from jde.models import F41001
from jde.models import F0116
from jde.models import F0005
from jde.models import F0115
from jde.models import F01151
from jde.models import F5842566
from jde.models import F0111
from jde.models import F4006


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
    def get(self, _text):

        try:
            connection.close()
            registro = User.objects.filter(
                Q(username__icontains=_text) |
                Q(first_name__icontains=_text) |
                Q(last_name__icontains=_text)
            ).order_by('date_joined')
            return registro

        except Exception:
            pass

    @classmethod
    def add(self, _username, _first_name, _last_name, _password, _estafeta_ambiente_clave):

        try:
            connection.close()
            usuario = User()
            usuario.username = _username
            usuario.first_name = _first_name
            usuario.last_name = _last_name
            if _password != '':
                usuario.set_password(_password)
            else:
                usuario.set_password("12345")
            usuario.save()

            estafeta_ambiente = ModeloEstafetaAmbiente.get(_estafeta_ambiente_clave)
            if len(estafeta_ambiente):
                usuario.profile.estafeta = estafeta_ambiente[0]
                usuario.profile.save()

        except Exception as e:
            print str(e)

    @classmethod
    def edit(self, _username, _first_name, _last_name, _password, _active, _estafeta_ambiente_clave):

        try:
            connection.close()
            usuario = User.objects.get(username=_username)
            usuario.first_name = _first_name
            usuario.last_name = _last_name
            usuario.is_active = _active

            if _password != '':
                usuario.set_password(_password)

            usuario.save()

            estafeta_ambiente = ModeloEstafetaAmbiente.get(_estafeta_ambiente_clave)
            if len(estafeta_ambiente):
                usuario.profile.estafeta = estafeta_ambiente[0]
                usuario.profile.save()

        except Exception as e:
            print str(e)


class ModeloEstafetaAmbiente(object):

    @classmethod
    def get(self, _text):

        try:
            connection.close()

            if _text:
                records = EstafetaAmbiente.objects.filter(
                    Q(clave__icontains=_text) |
                    Q(url__icontains=_text) |
                    Q(login__icontains=_text) |
                    Q(customer_number__icontains=_text)
                )
            else:
                records = EstafetaAmbiente.objects.all().order_by('created_date')
            return records

        except Exception as e:
            print str(e)

    @classmethod
    def get_Actives(self):

        try:
            connection.close()
            records = EstafetaAmbiente.objects.filter(is_active=True).order_by('created_date')
            return records

        except Exception as e:
            print str(e)

    @classmethod
    def add(self,
            _clave,
            _url,
            _login,
            _password,
            _quadrant,
            _suscriber_id,
            _paper_type,
            _is_active,
            _customer_number,
            _cot_url,
            _cot_id_usuario,
            _cot_usuario,
            _cot_contra):

        try:
            connection.close()
            registro = EstafetaAmbiente()
            registro.clave = _clave
            registro.url = _url
            registro.login = _login
            registro.password = _password
            registro.quadrant = _quadrant
            registro.suscriber_id = _suscriber_id
            registro.paper_type = _paper_type
            registro.is_active = _is_active
            registro.customer_number = _customer_number
            registro.cot_url = _cot_url
            registro.cot_id_usuario = _cot_id_usuario
            registro.cot_usuario = _cot_usuario
            registro.cot_contra = _cot_contra
            registro.save()

        except Exception as e:
            print str(e)

    @classmethod
    def edit(self,
             _clave,
             _url,
             _login,
             _password,
             _quadrant,
             _suscriber_id,
             _paper_type,
             _is_active,
             _customer_number,
             _cot_url,
             _cot_id_usuario,
             _cot_usuario,
             _cot_contra):

        try:
            connection.close()
            registro = EstafetaAmbiente.objects.get(clave=_clave)
            registro.login = _login
            registro.url = _url
            registro.password = _password
            registro.quadrant = _quadrant
            registro.suscriber_id = _suscriber_id
            registro.paper_type = _paper_type
            registro.is_active = _is_active
            registro.customer_number = _customer_number
            registro.cot_url = _cot_url
            registro.cot_id_usuario = _cot_id_usuario
            registro.cot_usuario = _cot_usuario
            registro.cot_contra = _cot_contra
            registro.save()

        except Exception as e:
            print str(e)


class Factura(object):

    @classmethod
    def get(self, _numero, _tipo):

        try:
            connection.close()
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

    # @classmethod
    # def InsertaGuia(self, _guia, _numero, _tipo):

    #     try:
    #         connection.close()
    #         factura = F5842566(using='jde')
    #         factura.TNDOC = _numero
    #         factura.TNDCT = _tipo
    #         factura.TNVR03 = _guia
    #         factura.TNUSER = 'JDE'
    #         factura.TNJOBN = 'IGPLENT1'
    #         factura.TNUPMJ = (1000 * (int(time.strftime("%Y")) - 1900) + int(time.strftime("%j")))
    #         factura.TNUPMT = int(time.strftime("%I%M%S"))
    #         factura.save()

    #     except Exception as error:
    #         value = {
    #             'mensaje': str(error)
    #         }
    #         return False, value

    # @classmethod
    # def ActualizaVtas(self, _numero, _tipo, _value):

    #     try:
    #         connection.close()
    #         factura = F4211.objects.using('jde').filter(
    #             SDDOC=_numero,
    #             SDDCT=_tipo
    #         )

    #         if len(factura) == 0:
    #             factura = F42119.objects.using('jde').filter(
    #                 SDDOC=_numero,
    #                 SDDCT=_tipo
    #             )

    #         for f in factura:
    #             f.SDVR03 = _value
    #             f.save()

    #     except Exception as error:
    #         value = {
    #             'mensaje': str(error)
    #         }
    #         return False, value


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
            connection.close()
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
                    corporatename = "%s %s" % (
                        direccion[0].ABALPH.strip(),
                        dir_complemento[0].ALADD1.strip()
                    )
                    datos['corporatename'] = corporatename[0:29]
                    datos["address1"] = dir_complemento[0].ALADD2.strip()
                    datos["address2"] = dir_complemento[0].ALADD3.strip()
                    datos['city'] = dir_complemento[0].ALCTY1.strip()
                    # datos['customernumber'] = dir_complemento[0] <-- Usuario Estafeta
                    datos['neighborhood'] = dir_complemento[0].ALADD4.strip()
                    datos['zipcode'] = dir_complemento[0].ALADDZ.strip()

                    if len(UDCestado) > 0:
                        datos['state'] = "%s" % (UDCestado[0].DRDL01.strip())

                    if len(direccion_Tel) > 0:
                        datos['phonenumber'] = "%s %s" % (
                            direccion_Tel[0].WPAR1,
                            direccion_Tel[0].WPPH1.strip()
                        )
                    if len(direccion_Resp) > 0:
                        datos['contactname'] = direccion_Resp[0].WWALPH.strip()[0:29]

                    if len(direccion_Cel) > 0:
                        datos['cellphone'] = "%s %s" % (
                            direccion_Cel[0].WPAR1,
                            direccion_Cel[0].WPPH1.strip()
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
            connection.close()
            factura = F4211.objects.using('jde').filter(
                SDDOC=_numero,
                SDDCT=_tipo
            )

            if len(factura) == 0:
                factura = F42119.objects.using('jde').filter(
                    SDDOC=_numero,
                    SDDCT=_tipo
                )

            if len(factura) > 0:

                CustomerNumber = str(factura[0].SDSHAN)
                if len(CustomerNumber) < 7:
                    cantidad = 7 - len(CustomerNumber)
                    sufijo = "0" * cantidad
                    datos['customernumber'] = "%s%s" % (sufijo, CustomerNumber)
                else:
                    datos['customernumber'] = str(factura[0].SDSHAN)

                if factura[0].SDSHAN < 199991:

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

                    if len(dir_complementoDestino) > 0:
                        corporate = "%s %s" % (
                            direccionDest[0].ABALPH.strip(),
                            dir_complementoDestino[0].ALADD1.strip()
                        )
                        datos['corporatename'] = corporate[0:29]
                        datos["address1"] = dir_complementoDestino[0].ALADD2.strip()
                        datos["address2"] = dir_complementoDestino[0].ALADD3.strip()
                        datos['city'] = dir_complementoDestino[0].ALCTY1.strip()
                        # datos['customernumber'] = dir_complementoDestino[0] <-- Usuario Estafeta
                        datos['neighborhood'] = dir_complementoDestino[0].ALADD4.strip()
                        datos['zipcode'] = dir_complementoDestino[0].ALADDZ.strip()
                        datos['Country'] = dir_complementoDestino[0].ALCTR.strip()
                        if len(UDCestadoDest) > 0:
                            datos['state'] = "%s" % (UDCestadoDest[0].DRDL01.strip())

                        if len(direccionDest_Tel) > 0:
                            datos['phonenumber'] = "%s %s" % (
                                direccionDest_Tel[0].WPAR1,
                                direccionDest_Tel[0].WPPH1.strip()
                            )
                        if len(direccionDest_Resp) > 0:
                            datos['contactname'] = direccionDest_Resp[0].WWALPH.strip()[0:29]

                        if len(direccionDest_Cel) > 0:
                            datos['cellphone'] = "%s %s" % (
                                direccionDest_Cel[0].WPAR1,
                                direccionDest_Cel[0].WPPH1.strip()
                            )

                if factura[0].SDSHAN >= 199991 and factura[0].SDSHAN <= 199999:

                    direccionDest = F4006.objects.using('jde').filter(
                        OAANTY__contains=2,
                        OADOCO=factura[0].SDDOCO,
                        OADCTO=factura[0].SDDCTO
                    )

                    UDCestadoDest = F0005.objects.using('jde').filter(
                        DRSY__contains='00',
                        DRRT__contains='S',
                        DRKY__contains=direccionDest[0].OAADDS
                    )

                    if len(direccionDest) > 0:
                        corporatename = "%s %s" % (
                            direccionDest[0].OAMLNM.strip(),
                            direccionDest[0].OAADD1.strip()
                        )

                        datos['corporatename'] = corporatename[0:29]
                        datos['contactname'] = direccionDest[0].OAMLNM.strip()[0:29]
                        datos["address1"] = direccionDest[0].OAADD2.strip()
                        datos["address2"] = direccionDest[0].OAADD3.strip()
                        datos['city'] = direccionDest[0].OACTY1.strip()
                        datos['neighborhood'] = direccionDest[0].OAADD4.strip()
                        datos['zipcode'] = direccionDest[0].OAADDZ.strip()
                        datos['Country'] = direccionDest[0].OACTR.strip()
                    if len(UDCestadoDest) > 0:
                        datos['state'] = "%s" % (UDCestadoDest[0].DRDL01.strip())

            return True, datos

        except Exception as error:
            value = {
                'mensaje': str(error)
            }
            return False, value
