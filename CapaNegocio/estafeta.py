import requests
# import ssl
import os
import binascii
from datetime import datetime
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

    def set_Servicio(self, _cliente_no, _numero_etiquetas,
                     _oficina_numero, _informacion_adicional,
                     _contenido, _descripcion_contenido,
                     _centro_costo, _entregar_en_estafeta,
                     _pais_destino, _cp_origen, _tipo_empaque,
                     _referencia, _documento_retorno,
                     _tipo_servicio, _peso):

        modulo = """<customerNumber xsi:type="ns2:string">%s</customerNumber>
                    <labelDescriptionList xsi:type="ns4:LabelDescriptionList">
                        <effectiveDate xsi:type="ns2:string" xsi:nil="true"/>
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
            _cliente_no,
            self.modulo_direccion_origen,
            self.modulo_direccion_destino,
            self.modulo_direccion_alternativa,
            _numero_etiquetas,
            _oficina_numero,
            _informacion_adicional,
            _contenido,
            _descripcion_contenido,
            _centro_costo,
            _entregar_en_estafeta,
            _pais_destino,
            _cp_origen,
            _tipo_empaque,
            _referencia,
            _documento_retorno,
            _tipo_servicio,
            _peso
        )

    def set_Credenciales(self, _login, _paper_type, _password, _quadrant, _suscribeid):

        modulo = """<login xsi:type="ns2:string">%s</login>
                    <paperType xsi:type="ns2:int">%s</paperType>
                    <password xsi:type="ns2:string">%s</password>
                    <quadrant xsi:type="ns2:int">%s</quadrant>
                    <suscriberId xsi:type="ns2:string">%s</suscriberId>
                    <valid xsi:type="ns2:boolean">true</valid>"""

        self.modulo_credenciales = modulo % (
            _login,
            _paper_type,
            _password,
            _quadrant,
            _suscribeid
        )

    def set_DireccionOrigen(self, _direccion1, _direccion2,
                            _cellphone, _city, _contactname,
                            _corporatename, _customernumber, _neighborhood,
                            _phonenumber, _state, _zipCode):

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
          _direccion1,
          _direccion2,
          _cellphone,
          _city,
          _contactname,
          _corporatename,
          _customernumber,
          _neighborhood,
          _phonenumber,
          _state,
          _zipCode)

    def set_DireccionDestino(self, _direccion1, _direccion2,
                             _cellphone, _city, _contactname,
                             _corporatename, _customernumber, _neighborhood,
                             _phonenumber, _state, _zipCode):

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
            _direccion1,
            _direccion2,
            _cellphone,
            _city,
            _contactname,
            _corporatename,
            _customernumber,
            _neighborhood,
            _phonenumber,
            _state,
            _zipCode)

    def set_DireccionAlternativa(self, _direccion1, _direccion2,
                                 _cellphone, _city, _contactname,
                                 _corporatename, _customernumber, _neighborhood,
                                 _phonenumber, _state, _zipCode):

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
            _direccion1,
            _direccion2,
            _cellphone,
            _city,
            _contactname,
            _corporatename,
            _customernumber,
            _neighborhood,
            _phonenumber,
            _state,
            _zipCode)

    def create_Response_File(self, _response):
        carpeta = Carpeta(os.path.abspath(os.path.join(os.getcwd())))
        archivo_response = Archivo(carpeta, "response.xml")
        archivo_response.write(_response)

    def get_ResponseEstado(self, _root):
        nodo = _root[0].xpath("//multiRef[@id = '%s']" % "id1")

        return nodo[0].find('resultDescription').text

    def get_ResponseEtiqueta(self, _root):
        nodo = _root[0].xpath("//multiRef[@id = '%s']" % "id0")
        resultado = nodo[0].find('labelPDF').text

        return resultado

    def create_ArchivoPdf(self, _contenido, _fac_tipo, _fac_numero):
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

    def create_ArchivoLog(self, _fac_tipo, _fac_numero):

        abspath_dir = self.create_DirectorioLog()

        namefile = "%s_%s.pdf" % (
            _fac_tipo,
            _fac_numero,
        )

        print abspath_dir

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

    def send(self, _factura_numero, _factura_tipo):

        # ssl._create_default_https_context = ssl._create_unverified_context
        base = self.get_Base()
        body = base % (self.modulo_servicio, self.modulo_credenciales)

        try:

            # Se genera la peticion
            response = requests.post(self.url, data=body.encode('utf-8'), headers=self.get_Header(), verify=False)

            self.create_Response_File(response.content.encode('utf-8'))

            if response.status_code == 200:
                root = etree.fromstring(response.content)
                response_estado = self.get_ResponseEstado(root)

                if response_estado == "OK":
                    texto_etiqueta = self.get_ResponseEtiqueta(root)
                    self.create_ArchivoPdf(texto_etiqueta, _factura_tipo, _factura_numero)
                    self.create_ArchivoLog(_factura_tipo, _factura_numero)
                    resultado = texto_etiqueta
                    bandera = True

                else:
                    resultado = response_estado
                    bandera = False

            else:
                resultado = response.content
                bandera = False

            return bandera, resultado

        except Exception, error:
            return False, str(error)


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

    def send(self):

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
            response = requests.post(
                self.url,
                data=body.encode('utf-8'),
                headers=self.get_Header(),
                verify=False
            )

            if response.status_code == 200:
                resultado = response.content
                bandera = False

            else:
                resultado = response.content
                bandera = False

            return bandera, resultado

        except Exception as e:
            return False, str(e)
