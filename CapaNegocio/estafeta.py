import requests
# import ssl
import os
from datetime import date
import binascii
from datetime import datetime
from datetime import timedelta
from wand.image import Image

from lxml import etree
from libtools.filesystem import Archivo
from libtools.filesystem import Carpeta
from libtools.filesystem import Error


class CreateLabelWS:

    def __init__(self, _url):

        self.url = _url
        self.modulo_direccion_origen = None
        self.modulo_direccion_destino = None
        self.modulo_direccion_alternativa = None
        self.modulo_credenciales = None
        self.modulo_servicio = None

    def get_Base(self):

        modulo = """<?xml version="1.0" encoding="UTF-8"?>
                    <SOAP-ENV:Envelope xmlns:ns3="http://schemas.xmlsoap.org/soap/encoding/"
                        xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                        xmlns:ns0="http://estafetalabel.webservices.estafeta.com"
                        xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/"
                        xmlns:ns2="http://www.w3.org/2001/XMLSchema"
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                        xmlns:ns4="http://dto.estafetalabel.webservices.estafeta.com"
                        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                    SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
                    <SOAP-ENV:Header/>
                       <ns1:Body>
                            <ns0:createLabel>
                                <in0 xsi:type="ns4:EstafetaLabelRequest">
                                %s
                                %s
                                </in0>
                            </ns0:createLabel>
                       </ns1:Body>
                    </SOAP-ENV:Envelope>"""

        return modulo

    def get_Header(self):
        cabecera = {
            'SOAPAction': '"https://label.estafeta.com/EstafetaLabel20/services/EstafetaLabelWS"',
            'Content-type': 'text/xml; charset="UTF-8"'
        }

        return cabecera

    def get_EfectiveDate(self):
        fecha = datetime.now()
        fecha_futura = fecha + timedelta(days=7)
        fecha_efectiva = fecha_futura.strftime('%Y%m%d')
        return fecha_efectiva

    def set_Servicio(self, _data):

        modulo = """<customerNumber xsi:type="ns2:string">%s</customerNumber>
                    <labelDescriptionList xsi:type="ns4:LabelDescriptionList">
                        <effectiveDate xsi:type="ns2:string">%s</effectiveDate>
                        %s
                        %s
                        %s
                        <numberOfLabels xsi:type="ns2:int">%s</numberOfLabels>
                        <officeNum xsi:type="ns2:string">%s</officeNum>
                        <aditionalInfo xsi:type="ns2:string">%s</aditionalInfo>
                        <content xsi:type="ns2:string">%s</content>
                        <contentDescription xsi:type="ns2:string">%s</contentDescription>
                        <costCenter xsi:type="ns2:string">%s</costCenter>
                        <deliveryToEstafetaOffice xsi:type="ns2:boolean">%s</deliveryToEstafetaOffice>
                        <destinationCountryId xsi:type="ns2:string">%s</destinationCountryId>
                        <originZipCodeForRouting xsi:type="ns2:string">%s</originZipCodeForRouting>
                        <parcelTypeId xsi:type="ns2:int">%s</parcelTypeId>
                        <reference xsi:type="ns2:string">%s</reference>
                        <returnDocument xsi:type="ns2:boolean">%s</returnDocument>
                        <serviceTypeId xsi:type="ns2:string">%s</serviceTypeId>
                        <serviceTypeIdDocRet xsi:type="ns2:string" xsi:nil="true"/>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <weight xsi:type="ns2:float">%s</weight>

                    </labelDescriptionList>
                    <labelDescriptionListCount xsi:type="ns2:int">1</labelDescriptionListCount>"""

        self.modulo_servicio = modulo % (
            _data['customer_number'],
            self.get_EfectiveDate(),
            self.modulo_direccion_origen,
            self.modulo_direccion_destino,
            self.modulo_direccion_alternativa,
            _data['number_labels'],
            _data['office_num'],
            _data['aditionalinfo'],
            _data['content'],
            _data['contentdescription'],
            _data['costcenter'],
            _data['deliverytoestafetaoffice'],
            _data['destino_countryid'],
            _data['cp_origen'],
            _data['parcelTypeId'],
            _data['reference'],
            _data['returndocument'],
            _data['servicetypeid'],
            _data['peso']
        )

    def set_Credenciales(self, _data):

        modulo = """<login xsi:type="ns2:string">%s</login>
                    <paperType xsi:type="ns2:int">%s</paperType>
                    <password xsi:type="ns2:string">%s</password>
                    <quadrant xsi:type="ns2:int">%s</quadrant>
                    <suscriberId xsi:type="ns2:string">%s</suscriberId>
                    <valid xsi:type="ns2:boolean">true</valid>"""

        self.modulo_credenciales = modulo % (
            _data['login'],
            _data['tipo_papel'],
            _data['password'],
            _data['quadrant'],
            _data['suscriber_id']
        )

    def set_DireccionOrigen(self, _data):

        modulo = """<originInfo xsi:type="ns4:OriginInfo">
                       <address1 xsi:type="ns2:string">%s</address1>
                       <address2 xsi:type="ns2:string">%s</address2>
                       <cellPhone xsi:type="ns2:string">%s</cellPhone>
                       <city xsi:type="ns2:string">%s</city>
                       <contactName xsi:type="ns2:string">%s</contactName>
                       <corporateName xsi:type="ns2:string">%s</corporateName>
                       <customerNumber xsi:type="ns2:string">%s</customerNumber>
                       <neighborhood xsi:type="ns2:string">%s</neighborhood>
                       <phoneNumber xsi:type="ns2:string">%s</phoneNumber>
                       <state xsi:type="ns2:string">%s</state>
                       <valid xsi:type="ns2:boolean">true</valid>
                       <zipCode xsi:type="ns2:string">%s</zipCode>
                   </originInfo>"""

        self.modulo_direccion_origen = modulo % (
          _data['origen_address1'],
          _data['origen_address2'],
          _data['origen_cellphone'],
          _data['origen_city'],
          _data['origen_contactname'],
          _data['origen_corporatename'],
          _data['customer_number'],
          _data['origen_neighborhood'],
          _data['origen_phonenumber'],
          _data['origen_state'],
          _data['origen_zipcode'])

    def set_DireccionDestino(self, _data):

        modulo = """<destinationInfo xsi:type="ns4:DestinationInfo">
                        <address1 xsi:type="ns2:string">%s</address1>
                        <address2 xsi:type="ns2:string">%s</address2>
                        <cellPhone xsi:type="ns2:string">%s</cellPhone>
                        <city xsi:type="ns2:string">%s</city>
                        <contactName xsi:type="ns2:string">%s</contactName>
                        <corporateName xsi:type="ns2:string">%s</corporateName>
                        <customerNumber xsi:type="ns2:string">%s</customerNumber>
                        <neighborhood xsi:type="ns2:string">%s</neighborhood>
                        <phoneNumber xsi:type="ns2:string">%s</phoneNumber>
                        <state xsi:type="ns2:string">%s</state>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <zipCode xsi:type="ns2:string">%s</zipCode>
                    </destinationInfo>"""

        self.modulo_direccion_destino = modulo % (
          _data['destino_address1'],
          _data['destino_address2'],
          _data['destino_cellphone'],
          _data['destino_city'],
          _data['destino_contactname'],
          _data['destino_corporatename'],
          _data['destino_customernumber'],
          _data['destino_neighborhood'],
          _data['destino_phonenumber'],
          _data['destino_state'],
          _data['destino_zipcode'])

    def set_DireccionAlternativa(self, _data):

        modulo = """<DRAlternativeInfo xsi:type="ns4:DRAlternativeInfo">
                        <address1 xsi:type="ns2:string">%s</address1>
                        <address2 xsi:type="ns2:string">%s</address2>
                        <cellPhone xsi:type="ns2:string">%s</cellPhone>
                        <city xsi:type="ns2:string">%s</city>
                        <contactName xsi:type="ns2:string">%s</contactName>
                        <corporateName xsi:type="ns2:string">%s</corporateName>
                        <customerNumber xsi:type="ns2:string">%s</customerNumber>
                        <neighborhood xsi:type="ns2:string">%s</neighborhood>
                        <phoneNumber xsi:type="ns2:string">%s</phoneNumber>
                        <state xsi:type="ns2:string">%s</state>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <zipCode xsi:type="ns2:string">%s</zipCode>
                    </DRAlternativeInfo>"""

        self.modulo_direccion_alternativa = modulo % (
          _data['destino_address1'],
          _data['destino_address2'],
          _data['destino_cellphone'],
          _data['destino_city'],
          _data['destino_contactname'],
          _data['destino_corporatename'],
          _data['destino_customernumber'],
          _data['destino_neighborhood'],
          _data['destino_phonenumber'],
          _data['destino_state'],
          _data['destino_zipcode'])

    def create_Request_File(self, _fac_tipo, _fac_numero, _response):
        carpeta = Carpeta(os.path.abspath(os.path.join(os.getcwd(), "wsfiles")))
        file_name = "createlabel_request_%s_%s.xml" % (_fac_tipo, _fac_numero)
        archivo_response = Archivo(carpeta, file_name)
        archivo_response.write(_response)

    def create_Response_File(self, _fac_tipo, _fac_numero, _response):
        carpeta = Carpeta(os.path.abspath(os.path.join(os.getcwd(), "wsfiles")))
        file_name = "createlabel_response_%s_%s.xml" % (_fac_tipo, _fac_numero)
        archivo_response = Archivo(carpeta, file_name)
        archivo_response.write(_response)

    def get_ResponseEstado(self, _root):
        nodo = _root[0].xpath("//multiRef[@id = '%s']" % "id1")

        return nodo[0].find('resultDescription').text

    def get_ResponseEtiqueta(self, _root):
        nodo = _root[0].xpath("//multiRef[@id = '%s']" % "id0")
        resultado = nodo[0].find('labelPDF').text

        return resultado

    def get_ResponseGuia(self, _root):
        nodo = _root[0].xpath("//multiRef[@id = '%s']" % "id2")

        return nodo[0].find('resultDescription').text

    def create_ArchivoPdf(self, _contenido, _fac_tipo, _fac_numero):
        abspath = os.path.abspath(os.path.join(os.getcwd(), "etiquetas"))
        namefile = "create_%s_%s.pdf" % (
            _fac_tipo,
            _fac_numero
        )
        carpeta = Carpeta(abspath)
        archivo = Archivo(carpeta, namefile)

        label_binary_data = binascii.a2b_base64(_contenido)
        archivo.write(label_binary_data)

        self.create_Image(archivo)

        return archivo

    def create_DirectorioLog(self):
        new_abspath = ""

        try:
            abspath = os.path.abspath(os.path.join(os.getcwd(), "logs"))

            carpeta = Carpeta(abspath)

            ahora = datetime.now()
            new_directorios = [
                '{:02d}'.format(ahora.year),
                '{:02d}'.format(ahora.month),
                '{:02d}'.format(ahora.day)
            ]

            carpeta.add_Folders(new_directorios)

        except Exception as e:
            if isinstance(e, Error):
                if e.control == 'carpeta ya existe':
                    new_abspath = os.path.join(carpeta.abspath, *new_directorios)

            else:
                raise ValueError(str(e))

        return new_abspath

    def create_ArchivoLog(self, _fac_tipo, _fac_numero, _guias, _username):

        abspath_dir = self.create_DirectorioLog()

        namefile = "%s_%s_%s.log" % (
            _fac_tipo,
            _fac_numero,
            _username
        )

        folder = Carpeta(abspath_dir)
        archivo = Archivo(folder, namefile)
        ahora = datetime.now()
        template = """Factura Tipo: %s \nFactura Numero: %s \nUsuario: %s \nFecha: %s \nNo. Guia(s): \n%s"""
        texto = template % (_fac_tipo, _fac_numero, _username, str(ahora.strftime("%d/%m/%Y %H:%M:%S")), _guias)

        archivo.write(texto)

    def create_Image(self, _file_pdf):

        try:
            archivo = "%s%s" % (_file_pdf.get_Abspath(), "[0]")
            with Image(filename=archivo) as img:
                img.alpha_channel = True
                img.format = 'png'
                file_image = _file_pdf.get_Abspath().replace("pdf", "png")
                img.save(filename=file_image)
        except Exception:
            pass

    def send(self, _factura_numero, _factura_tipo, _username):

        # ssl._create_default_https_context = ssl._create_unverified_context
        base = self.get_Base()
        body = base % (self.modulo_servicio, self.modulo_credenciales)

        try:
            self.create_Request_File(
                _factura_tipo,
                _factura_numero,
                body.encode('utf-8')
            )

            # Se genera la peticion
            response = requests.post(self.url, data=body.encode('utf-8'), headers=self.get_Header(), verify=False)

            self.create_Response_File(
                _factura_tipo,
                _factura_numero,
                response.content.encode('utf-8')
            )

            if response.status_code == 200:
                root = etree.fromstring(response.content)
                response_estado = self.get_ResponseEstado(root)

                if response_estado == "OK":
                    texto_etiqueta = self.get_ResponseEtiqueta(root)
                    guia = self.get_ResponseGuia(root)

                    archivo_pdf = self.create_ArchivoPdf(texto_etiqueta, _factura_tipo, _factura_numero, guia)
                    self.create_ArchivoLog(_factura_tipo, _factura_numero, guia, _username)
                    resultado = texto_etiqueta
                    bandera = True

                else:
                    resultado = response_estado
                    guia = "0"
                    bandera = False
                    archivo_pdf = None

            else:
                resultado = response.content
                guia = "0"
                bandera = False
                archivo_pdf = None

            return bandera, resultado, guia, archivo_pdf

        except Exception, error:
            return False, str(error), "", None


class ReprintLabelWS:

    def __init__(self, _url):

        self.url = _url
        self.modulo_credenciales = None
        self.modulo_direccion_origen = None
        self.modulo_direccion_destino = None
        self.modulo_direccion_alternativa = None
        self.modulo_servicio = None

    def get_EfectiveDate(self):
        fecha = datetime.now()
        fecha_futura = fecha + timedelta(days=7)
        fecha_efectiva = fecha_futura.strftime('%Y%m%d')
        return fecha_efectiva

    def get_Header(self):
        cabecera = {
            'SOAPAction': '"https://label.estafeta.com/EstafetaLabel20/services/EstafetaLabelWS"',
            'Content-type': 'text/xml; charset="UTF-8"'
        }

        return cabecera

    def get_Base(self):

        modulo = """<?xml version="1.0" encoding="UTF-8"?>
                    <SOAP-ENV:Envelope xmlns:ns3="http://schemas.xmlsoap.org/soap/encoding/"
                        xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                        xmlns:ns0="http://estafetalabel.webservices.estafeta.com"
                        xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/"
                        xmlns:ns2="http://www.w3.org/2001/XMLSchema"
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                        xmlns:ns4="http://dto.estafetalabel.webservices.estafeta.com"
                        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                    SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
                    <SOAP-ENV:Header/>
                       <ns1:Body>
                            <ns0:createLabel>
                                <in0 xsi:type="ns4:EstafetaReprintLabelRequest">
                                %s
                                </in0>
                            </ns0:createLabel>
                       </ns1:Body>
                    </SOAP-ENV:Envelope>"""

        return modulo

    def set_Credenciales(self, _data):

        modulo = """<quadrant xsi:type="ns2:int">%s</quadrant>
                    <valid xsi:type="ns2:boolean">true</valid>
                    <password xsi:type="ns2:string">%s</password>
                    <ReprintLabelDescriptionCount xsi:type="ns2:int">1</ReprintLabelDescriptionCount>
                    <login xsi:type="ns2:string">%s</login>
                    <customerNumber xsi:type="ns2:string">%s</customerNumber>
                    %s
                    <suscriberId xsi:type="ns2:string">%s</suscriberId>
                    <paperType xsi:type="ns2:int">%s</paperType>"""

        self.modulo_credenciales = modulo % (
            _data['quadrant'],
            _data['password'],
            _data['login'],
            _data['customer_number'],
            self.modulo_servicio,
            _data['suscriber_id'],
            _data['tipo_papel']
        )

    def set_Servicio(self, _data):

        modulo = """<labelDescriptionList xsi:type="ns4:LabelDescriptionList">
                        <aditionalInfo xsi:type="ns2:string">%s</aditionalInfo>
                        <content xsi:type="ns2:string">%s</content>
                        <costCenter xsi:type="ns2:string">%s</costCenter>
                        <deliveryToEstafetaOffice xsi:type="ns2:boolean">%s</deliveryToEstafetaOffice>
                        <destinationCountryId xsi:type="ns2:string">%s</destinationCountryId>
                        %s
                        %s
                        <parcelTypeId xsi:type="ns2:int">%s</parcelTypeId>
                        <reference xsi:type="ns2:string">%s</reference>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <weight xsi:type="ns2:float">%s</weight>
                        <effectiveDate xsi:type="ns2:string">%s</effectiveDate>
                        <contentDescription xsi:type="ns2:string">%s</contentDescription>
                        <parcelNumber xsi:type="ns2:string">%s</parcelNumber>


                    </labelDescriptionList>
                    <labelDescriptionListCount xsi:type="ns2:int">1</labelDescriptionListCount>"""

        self.modulo_servicio = modulo % (
            _data['aditionalinfo'],
            _data['content'],
            _data['costcenter'],
            _data['deliverytoestafetaoffice'],
            _data['destino_countryid'],
            self.modulo_direccion_destino,
            self.modulo_direccion_origen,
            _data['parcelTypeId'],
            _data['reference'],
            _data['peso'],
            self.get_EfectiveDate(),
            _data['contentdescription'],
            _data['parcelNumber'],
        )

    def set_DireccionOrigen(self, _data):

        modulo = """<originInfo xsi:type="ns4:OriginInfo">
                       <address1 xsi:type="ns2:string">%s</address1>
                       <address2 xsi:type="ns2:string">%s</address2>
                       <cellPhone xsi:type="ns2:string">%s</cellPhone>
                       <city xsi:type="ns2:string">%s</city>
                       <contactName xsi:type="ns2:string">%s</contactName>
                       <corporateName xsi:type="ns2:string">%s</corporateName>
                       <customerNumber xsi:type="ns2:string">%s</customerNumber>
                       <neighborhood xsi:type="ns2:string">%s</neighborhood>
                       <phoneNumber xsi:type="ns2:string">%s</phoneNumber>
                       <state xsi:type="ns2:string">%s</state>
                       <valid xsi:type="ns2:boolean">true</valid>
                       <zipCode xsi:type="ns2:string">%s</zipCode>
                   </originInfo>"""

        self.modulo_direccion_origen = modulo % (
          _data['origen_address1'],
          _data['origen_address2'],
          _data['origen_cellphone'],
          _data['origen_city'],
          _data['origen_contactname'],
          _data['origen_corporatename'],
          _data['customer_number'],
          _data['origen_neighborhood'],
          _data['origen_phonenumber'],
          _data['origen_state'],
          _data['origen_zipcode'])

    def set_DireccionDestino(self, _data):

        modulo = """<destinationInfo xsi:type="ns4:DestinationInfo">
                        <address1 xsi:type="ns2:string">%s</address1>
                        <address2 xsi:type="ns2:string">%s</address2>
                        <cellPhone xsi:type="ns2:string">%s</cellPhone>
                        <city xsi:type="ns2:string">%s</city>
                        <contactName xsi:type="ns2:string">%s</contactName>
                        <corporateName xsi:type="ns2:string">%s</corporateName>
                        <customerNumber xsi:type="ns2:string">%s</customerNumber>
                        <neighborhood xsi:type="ns2:string">%s</neighborhood>
                        <phoneNumber xsi:type="ns2:string">%s</phoneNumber>
                        <state xsi:type="ns2:string">%s</state>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <zipCode xsi:type="ns2:string">%s</zipCode>
                    </destinationInfo>"""

        self.modulo_direccion_destino = modulo % (
          _data['destino_address1'],
          _data['destino_address2'],
          _data['destino_cellphone'],
          _data['destino_city'],
          _data['destino_contactname'],
          _data['destino_corporatename'],
          _data['destino_customernumber'],
          _data['destino_neighborhood'],
          _data['destino_phonenumber'],
          _data['destino_state'],
          _data['destino_zipcode'])

    def set_DireccionAlternativa(self, _data):

        modulo = """<DRAlternativeInfo xsi:type="ns4:DRAlternativeInfo">
                        <address1 xsi:type="ns2:string">%s</address1>
                        <address2 xsi:type="ns2:string">%s</address2>
                        <cellPhone xsi:type="ns2:string">%s</cellPhone>
                        <city xsi:type="ns2:string">%s</city>
                        <contactName xsi:type="ns2:string">%s</contactName>
                        <corporateName xsi:type="ns2:string">%s</corporateName>
                        <customerNumber xsi:type="ns2:string">%s</customerNumber>
                        <neighborhood xsi:type="ns2:string">%s</neighborhood>
                        <phoneNumber xsi:type="ns2:string">%s</phoneNumber>
                        <state xsi:type="ns2:string">%s</state>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <zipCode xsi:type="ns2:string">%s</zipCode>
                    </DRAlternativeInfo>"""

        self.modulo_direccion_alternativa = modulo % (
          _data['destino_address1'],
          _data['destino_address2'],
          _data['destino_cellphone'],
          _data['destino_city'],
          _data['destino_contactname'],
          _data['destino_corporatename'],
          _data['destino_customernumber'],
          _data['destino_neighborhood'],
          _data['destino_phonenumber'],
          _data['destino_state'],
          _data['destino_zipcode'])

    def create_Request_File(self, _fac_tipo, _fac_numero, _response):
        carpeta = Carpeta(os.path.abspath(os.path.join(os.getcwd(), "wsfiles")))
        file_name = "reprintlabel_request_%s_%s.xml" % (_fac_tipo, _fac_numero)
        archivo_response = Archivo(carpeta, file_name)
        archivo_response.write(_response)

    def create_Response_File(self, _fac_tipo, _fac_numero, _response):
        carpeta = Carpeta(os.path.abspath(os.path.join(os.getcwd(), "wsfiles")))
        file_name = "reprintlabel_response_%s_%s.xml" % (_fac_tipo, _fac_numero)
        archivo_response = Archivo(carpeta, file_name)
        archivo_response.write(_response)

    def get_ResponseEstado(self, _root):
        nodo = _root[0].xpath("//multiRef[@id = '%s']" % "id1")

        return nodo[0].find('resultDescription').text

    def get_ResponseEtiqueta(self, _root):
        nodo = _root[0].xpath("//multiRef[@id = '%s']" % "id0")
        resultado = nodo[0].find('labelPDF').text

        return resultado

    def get_ResponseGuia(self, _root):
        nodo = _root[0].xpath("//multiRef[@id = '%s']" % "id2")

        return nodo[0].find('resultDescription').text

    def create_ArchivoPdf(self, _contenido, _fac_tipo, _fac_numero, _guia):
        abspath = os.path.abspath(os.path.join(os.getcwd(), "etiquetas"))
        namefile = "%s_%s.pdf" % (
            _fac_tipo,
            _fac_numero
        )
        carpeta = Carpeta(abspath)
        archivo = Archivo(carpeta, namefile)

        label_binary_data = binascii.a2b_base64(_contenido)
        archivo.write(label_binary_data)

        self.create_Image(archivo)

    def create_DirectorioLog(self):
        new_abspath = ""

        try:
            abspath = os.path.abspath(os.path.join(os.getcwd(), "logs"))

            carpeta = Carpeta(abspath)

            ahora = datetime.now()
            new_directorios = [
                '{:02d}'.format(ahora.year),
                '{:02d}'.format(ahora.month),
                '{:02d}'.format(ahora.day)
            ]

            carpeta.add_Folders(new_directorios)

        except Exception as e:
            if isinstance(e, Error):
                if e.control == 'carpeta ya existe':
                    new_abspath = os.path.join(carpeta.abspath, *new_directorios)

            else:
                raise ValueError(str(e))

        return new_abspath

    def create_ArchivoLog(self, _fac_tipo, _fac_numero, _guia, _username):

        abspath_dir = self.create_DirectorioLog()

        namefile = "%s_%s_%s.log" % (
            _fac_tipo,
            _fac_numero,
            _username
        )

        folder = Carpeta(abspath_dir)
        archivo = Archivo(folder, namefile)
        ahora = datetime.now()
        template = """Factura Tipo: %s \nFactura Numero: %s \nNo. Guia: %s \nUsuario: %s \nFecha: %s"""
        texto = template % (_fac_tipo, _fac_numero, _guia, _username, str(ahora.strftime("%d/%m/%Y %H:%M:%S")))

        archivo.write(texto)

    def create_Image(self, _file_pdf):

        try:
            archivo = "%s%s" % (_file_pdf.get_Abspath(), "[0]")
            with Image(filename=archivo) as img:
                img.alpha_channel = True
                img.format = 'png'
                file_image = _file_pdf.get_Abspath().replace("pdf", "png")
                img.save(filename=file_image)
        except Exception:
            pass

    def send(self, _factura_numero, _factura_tipo, _username):

        # ssl._create_default_https_context = ssl._create_unverified_context
        base = self.get_Base()
        body = base % (self.modulo_servicio, self.modulo_credenciales)

        try:
            self.create_Request_File(
                _factura_tipo,
                _factura_numero,
                body.encode('utf-8')
            )

            # Se genera la peticion
            response = requests.post(self.url, data=body.encode('utf-8'), headers=self.get_Header(), verify=False)

            self.create_Response_File(
                _factura_tipo,
                _factura_numero,
                response.content.encode('utf-8')
            )

            if response.status_code == 200:
                root = etree.fromstring(response.content)
                response_estado = self.get_ResponseEstado(root)

                if response_estado == "OK":
                    texto_etiqueta = self.get_ResponseEtiqueta(root)
                    guia = self.get_ResponseGuia(root)

                    self.create_ArchivoPdf(texto_etiqueta, _factura_tipo, _factura_numero, guia)
                    self.create_ArchivoLog(_factura_tipo, _factura_numero, guia, _username)
                    resultado = texto_etiqueta
                    bandera = True

                else:
                    resultado = response_estado
                    guia = "0"
                    bandera = False

            else:
                resultado = response.content
                guia = "0"
                bandera = False

            return bandera, resultado, guia

        except Exception, error:
            return False, str(error), ""


class CotizacionWS:

    def __init__(self, _url):

        self.url = _url
        self.modulo_origen = None
        self.modulo_destino = None
        self.modulo_tipo_envio = None
        self.modulo_es_lista = None
        self.modulo_es_frecuencia = None
        self.modulo_credenciales = None

    def get_Base(self):

        modulo = """<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                        <soap:Body>
                            <FrecuenciaCotizador xmlns="http://www.estafeta.com/">
                            %s
                            %s
                            %s
                            %s
                            %s
                            %s
                            </FrecuenciaCotizador>
                        </soap:Body>
                    </soap:Envelope>"""

        return modulo

    def get_Header(self):
        cabecera = {
            'Content-type': 'text/xml; charset="UTF-8"'
        }

        return cabecera

    def set_Credenciales(self, _id_usuario, _usuario, _contra):
        modulo = """<idusuario>%s</idusuario>
                    <usuario>%s</usuario>
                    <contra>%s</contra>"""

        self.modulo_credenciales = modulo % (
            _id_usuario,
            _usuario,
            _contra
        )

    def set_EsFrecuencia(self, _value):
        modulo = """<esFrecuencia>%s</esFrecuencia>"""

        self.modulo_es_frecuencia = modulo % (_value)

    def set_EsLista(self, _value):
        modulo = """<esLista>%s</esLista>"""

        self.modulo_es_lista = modulo % (_value)

    def set_TipoEnvio(self, _is_paquete, _largo, _peso, _alto, _ancho):
        modulo = """<tipoEnvio>
                        <EsPaquete>%s</EsPaquete>
                        <Largo>%s</Largo>
                        <Peso>%s</Peso>
                        <Alto>%s</Alto>
                        <Ancho>%s</Ancho>
                    </tipoEnvio>"""

        self.modulo_tipo_envio = modulo % (
            _is_paquete,
            _largo,
            _peso,
            _alto,
            _ancho
        )

    def set_Origen(self, _value):
        modulo = """<datosOrigen>
                        <string>%s</string>
                    </datosOrigen>"""

        self.modulo_origen = modulo % (_value)

    def set_Destino(self, _value):
        modulo = """<datosDestino>
                        <string>%s</string>
                    </datosDestino>"""

        self.modulo_destino = modulo % (_value)

    def create_Request_File(self, _fac_tipo, _fac_numero, _response):
        carpeta = Carpeta(os.path.abspath(os.path.join(os.getcwd(), "wsfiles")))
        file_name = "cotizacion_request_%s_%s.xml" % (_fac_tipo, _fac_numero)
        archivo_response = Archivo(carpeta, file_name)
        archivo_response.write(_response)

    def create_Response_File(self, _fac_tipo, _fac_numero, _response):
        carpeta = Carpeta(os.path.abspath(os.path.join(os.getcwd(), "wsfiles")))
        file_name = "cotizacion_response_%s_%s.xml" % (_fac_tipo, _fac_numero)
        archivo_response = Archivo(carpeta, file_name)
        archivo_response.write(_response)

    def get_ResponseEstado(self, _root):
        value = _root[0][0][0][0].find('{http://www.estafeta.com/}Error').text

        return value

    def get_ResponseError(self, _root):
        value = _root[0][0][0][0].find('{http://www.estafeta.com/}MensajeError').text

        return value

    def send(self, _factura_numero, _factura_tipo):

        base = self.get_Base()
        body = base % (
            self.modulo_credenciales,
            self.modulo_es_frecuencia,
            self.modulo_es_lista,
            self.modulo_tipo_envio,
            self.modulo_origen,
            self.modulo_destino
        )

        try:
            self.create_Request_File(
                _factura_tipo,
                _factura_numero,
                body
            )

            response = requests.post(
                self.url,
                data=body.encode('utf-8'),
                headers=self.get_Header(),
                verify=False
            )

            self.create_Response_File(
                _factura_tipo,
                _factura_numero,
                response.content
            )

            if response.status_code == 200:
                root = etree.fromstring(response.content)
                response_estado = self.get_ResponseEstado(root)

                if response_estado == "000":
                    resultado = response_estado
                    bandera = True

                else:
                    resultado = self.get_ResponseError(root)
                    bandera = False
            else:
                resultado = response.content
                bandera = False

            return bandera, resultado

        except Exception as e:
            return False, str(e)
