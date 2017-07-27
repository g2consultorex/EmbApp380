
class EstafetaWebService:

    def __init__(self, _url):

        # self.url = _url
        self.url = 'https://labelqa.estafeta.com/EstafetaLabel20/services/EstafetaLabelWS?wsdl'

    def get_CreateLabel_Header(self):
        cabecera = {
            'SOAPAction': '"https://label.estafeta.com/EstafetaLabel20/services/EstafetaLabelWS"',
            'Content-type': 'text/xml; charset="UTF-8"'
        }

        return cabecera

    def set_Destino(self, _direccion1, _direccion2,
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
