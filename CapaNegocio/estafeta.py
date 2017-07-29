import requests
import ssl


class EstafetaWebService:

    def __init__(self, _url):

        self.url = _url
        self.modulo_direccion_origen = None
        self.modulo_direccion_destino = None
        self.modulo_direccion_alternativa = None
        self.modulo_credenciales = None
        self.modulo_servicio = None

    def get_Base_CreateLabel(self):

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

    def get_CreateLabel_Header(self):
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
                            corporatename, customernumber, _neighborhood,
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
          corporatename,
          customernumber,
          _neighborhood,
          _phonenumber,
          _state,
          _zipCode)

    def set_DireccionDestino(self, _direccion1, _direccion2,
                             _cellphone, _city, _contactname,
                             corporatename, customernumber, _neighborhood,
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
            corporatename,
            customernumber,
            _neighborhood,
            _phonenumber,
            _state,
            _zipCode)

    def set_DireccionAlternativa(self, _direccion1, _direccion2,
                                 _cellphone, _city, _contactname,
                                 corporatename, customernumber, _neighborhood,
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
            corporatename,
            customernumber,
            _neighborhood,
            _phonenumber,
            _state,
            _zipCode)

    def create_Label(self):

        # ssl._create_default_https_context = ssl._create_unverified_context

        base = self.get_Base_CreateLabel()
        body = base % (self.modulo_servicio, self.modulo_credenciales)

        try:
            print body
            response = requests.post(self.url, data=body, headers=self.get_CreateLabel_Header(), verify=False)

            return response.content
            # return body

        except Exception, error:
            # import ipdb; ipdb.set_trace()
            return str(error)
