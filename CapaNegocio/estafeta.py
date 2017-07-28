
class EstafetaWebService:

    def __init__(self, _url):

        self.url = _url
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

    def set_Servicio(self):

        modulo = """<customerNumber xsi:type="ns2:string">%s</customerNumber>
                        <labelDescriptionList xsi:type="ns4:LabelDescriptionList">
                            <effectiveDate xsi:type="ns2:string" xsi:nil="true"/>
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
            "", # Aqui van las direcciones origen y destino
            _numero_etiquetas,
            _oficina_numero,
            _informacion_adicional,
            _contenido,
            _descripcion_contenido,
            _centro_costo,
            _entregar_en_estafeta,
            _pais_destino,
            "", # codigo postal destino
            "", # Tipo, paquete o sobre
            _referencia,
            _documento_retorno,
            _tipo_servicio,
            "" # Peso
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
                       <address1 xsi:type="ns2:string">%</address1>
                       <address2 xsi:type="ns2:string">%</address2>
                       <cellPhone xsi:type="ns2:string">%</cellPhone>
                       <city xsi:type="ns2:string">%</city>
                       <contactName xsi:type="ns2:string">%</contactName>
                       <corporateName xsi:type="ns2:string">%</corporateName>
                       <customerNumber xsi:type="ns2:string">%</customerNumber>
                       <neighborhood xsi:type="ns2:string">%</neighborhood>
                       <phoneNumber xsi:type="ns2:string">%</phoneNumber>
                       <state xsi:type="ns2:string">%</state>
                       <valid xsi:type="ns2:boolean">true</valid>
                       <zipCode xsi:type="ns2:string">%</zipCode>
                   </originInfo>"""

        value = modulo % (
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

        return value

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

        value = modulo % (
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

        return value

    def create_Label(self):
        base = self.get_Base_CreateLabel()
        body = base % (self.modulo_credenciales)

        return body
