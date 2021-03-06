<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
    xmlns:ns3="http://schemas.xmlsoap.org/soap/encoding/"
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
                <customerNumber xsi:type="ns2:string">0000000</customerNumber>
                <labelDescriptionList xsi:type="ns4:LabelDescriptionList">
                    <DRAlternativeInfo xsi:type="ns4:DRAlternativeInfo">
                        <address1 xsi:type="ns2:string">CERRADA DE CEYLAN</address1>
                        <address2 xsi:type="ns2:string">539</address2>
                        <cellPhone xsi:type="ns2:string">55555555</cellPhone>
                        <city xsi:type="ns2:string">AZCAPOTZALCO</city>
                        <contactName xsi:type="ns2:string">CARLOS MATEOS</contactName>
                        <corporateName xsi:type="ns2:string">INTERNET SA DE CV</corporateName>
                        <customerNumber xsi:type="ns2:string">0000000</customerNumber>
                        <neighborhood xsi:type="ns2:string">INDUSTRIAL</neighborhood>
                        <phoneNumber xsi:type="ns2:string">6666666666</phoneNumber>
                        <state xsi:type="ns2:string">DF</state>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <zipCode xsi:type="ns2:string">02300</zipCode>
                    </DRAlternativeInfo>
                    <aditionalInfo xsi:type="ns2:string">OPERACION5</aditionalInfo>
                    <content xsi:type="ns2:string">JOYAS</content>
                    <contentDescription xsi:type="ns2:string">ORO</contentDescription>
                    <costCenter xsi:type="ns2:string">12345</costCenter>
                    <deliveryToEstafetaOffice xsi:type="ns2:boolean">False</deliveryToEstafetaOffice>
                    <destinationCountryId xsi:type="ns2:string">MX</destinationCountryId>
                    <destinationInfo xsi:type="ns4:DestinationInfo">
                        <address1 xsi:type="ns2:string">MAIZALES</address1>
                        <address2 xsi:type="ns2:string">35</address2>
                        <cellPhone xsi:type="ns2:string">4444444</cellPhone>
                        <city xsi:type="ns2:string">COYOACAN</city>
                        <contactName xsi:type="ns2:string">JAVIER SANCHEZ</contactName>
                        <corporateName xsi:type="ns2:string">CHICOLOAPAN SA DE CV</corporateName>
                        <customerNumber xsi:type="ns2:string">0000000</customerNumber>
                        <neighborhood xsi:type="ns2:string">CENTRO</neighborhood>
                        <phoneNumber xsi:type="ns2:string">777777</phoneNumber>
                        <state xsi:type="ns2:string">ESTADO DE MEXICO</state>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <zipCode xsi:type="ns2:string">02130</zipCode>
                    </destinationInfo>
                    <effectiveDate xsi:type="ns2:string" xsi:nil="true"/>
                    <numberOfLabels xsi:type="ns2:int">1</numberOfLabels>
                    <officeNum xsi:type="ns2:string">130</officeNum>
                    <originInfo xsi:type="ns4:OriginInfo">
                        <address1 xsi:type="ns2:string">CALLE 5</address1>
                        <address2 xsi:type="ns2:string">29</address2>
                        <cellPhone xsi:type="ns2:string">888888</cellPhone>
                        <city xsi:type="ns2:string">TLALPAN</city>
                        <contactName xsi:type="ns2:string">JANET OIDOR</contactName>
                        <corporateName xsi:type="ns2:string">ALTAS SA DE CV</corporateName>
                        <customerNumber xsi:type="ns2:string">0000000</customerNumber>
                        <neighborhood xsi:type="ns2:string">CENTRO</neighborhood>
                        <phoneNumber xsi:type="ns2:string">9999999</phoneNumber>
                        <state xsi:type="ns2:string">DF</state>
                        <valid xsi:type="ns2:boolean">true</valid>
                        <zipCode xsi:type="ns2:string">02300</zipCode>
                    </originInfo>
                    <originZipCodeForRouting xsi:type="ns2:string">02300</originZipCodeForRouting>
                    <parcelTypeId xsi:type="ns2:int">1</parcelTypeId>
                    <reference xsi:type="ns2:string">FRENTE AL SANBORNS</reference>
                    <returnDocument xsi:type="ns2:boolean">false</returnDocument>
                    <serviceTypeId xsi:type="ns2:string">70</serviceTypeId>
                    <serviceTypeIdDocRet xsi:type="ns2:string" xsi:nil="true"/>
                    <valid xsi:type="ns2:boolean">true</valid>
                    <weight xsi:type="ns2:float">5</weight>
                </labelDescriptionList>
                <labelDescriptionListCount xsi:type="ns2:int">1</labelDescriptionListCount>
                <login xsi:type="ns2:string">prueba1</login>
                <paperType xsi:type="ns2:int">1</paperType>
                <password xsi:type="ns2:string">lAbeL_K_11</password>
                <quadrant xsi:type="ns2:int">0</quadrant>
                <suscriberId xsi:type="ns2:string">28</suscriberId>
                <valid xsi:type="ns2:boolean">true</valid>
            </in0>
        </ns0:createLabel>
    </ns1:Body>
</SOAP-ENV:Envelope>
