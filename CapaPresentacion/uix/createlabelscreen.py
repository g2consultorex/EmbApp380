# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
# from CapaPresentacion.uix.widget import Toast
# from CapaNegocio.gestordb import ModeloEstafetaAmbiente
# from CapaNegocio.gestordb import Factura
from CapaNegocio.gestordb import DireccionOrigen
from CapaNegocio.gestordb import DireccionDestino
from CapaNegocio.gestordb import ModeloUsuario
from CapaNegocio.gestordb import NuevoDestino
from CapaNegocio.gestordb import Factura
from CapaNegocio.gestordb import DeliveryInst

from CapaNegocio.estafeta import CreateLabelWS
from CapaNegocio.estafeta import ReprintLabelWS
from CapaNegocio.estafeta import CotizacionWS


class CreateLabelScreen(Screen):

    guia = ""
    is_reprint = False

    def __init__(self, **kwargs):
        super(CreateLabelScreen, self).__init__(**kwargs)
        self.factura_numero = ""
        self.factura_tipo = ""
        self.user_account = ""
        self._show_loader(False)

    def _show_loader(self, show):
        if show:
            self.ids['loader'].opacity = 1.0
        else:
            self.ids['loader'].opacity = 0.0

    def _show_toast(self, text):
        self.ids['toast'].show(text)

    def failure(self, error):
        self._show_toast(error)
        self._show_loader(False)

    def fill_DataOrigen(self, _data):
        data = self.ids['label_container'].ids['origen_widget']
        data.ids['txt_origen_address1'].text = _data["address1"]
        data.ids['txt_origen_address2'].text = _data["address2"]
        data.ids['txt_origen_cellphone'].text = _data["cellphone"]
        data.ids['txt_origen_city'].text = _data['city']
        data.ids['txt_origen_contactname'].text = _data["contactname"]
        data.ids['txt_origen_corporatename'].text = _data["corporatename"]
        data.ids['txt_origen_neighborhood'].text = _data['neighborhood']
        data.ids['txt_origen_phonenumber'].text = _data["phonenumber"]
        data.ids['txt_origen_state'].text = _data['state']
        data.ids['txt_origen_zipcode'].text = _data['zipcode']

    def clear_DataOrigen(self):
        data = self.ids['label_container'].ids['origen_widget']
        data.ids['txt_origen_address1'].text = ""
        data.ids['txt_origen_address2'].text = ""
        data.ids['txt_origen_cellphone'].text = ""
        data.ids['txt_origen_city'].text = ""
        data.ids['txt_origen_contactname'].text = ""
        data.ids['txt_origen_corporatename'].text = ""
        data.ids['txt_origen_neighborhood'].text = ""
        data.ids['txt_origen_phonenumber'].text = ""
        data.ids['txt_origen_state'].text = ""
        data.ids['txt_origen_zipcode'].text = ""

    def get_DataOrigen(self):
        data = {}
        fields = self.ids['label_container'].ids['origen_widget']

        if fields.ids['txt_origen_address1'].text != "":
            data['origen_address1'] = fields.ids['txt_origen_address1'].text

            if len(data['origen_address1']) > 30:
                raise ValueError("Direccion 1 en DIRECCION ORIGEN es mayor de 30")
        else:
            raise ValueError("Falta Direccion 1 en DIRECCION ORIGEN")

        if fields.ids['txt_origen_address2'].text != "":
            data['origen_address2'] = fields.ids['txt_origen_address2'].text

            if len(data['origen_address2']) > 30:
                raise ValueError("Direccion 2 en DIRECCION ORIGEN es mayor de 30")
        else:
            raise ValueError("Falta Direccion 2 en DIRECCION ORIGEN")

        if fields.ids['txt_origen_city'].text != "":
            data['origen_city'] = fields.ids['txt_origen_city'].text

            if len(data['origen_city']) > 50:
                raise ValueError("Ciudad en DIRECCION ORIGEN es mayor de 50")
        else:
            raise ValueError("Falta Ciudad en DIRECCION ORIGEN")

        if fields.ids['txt_origen_contactname'].text != "":
            data['origen_contactname'] = fields.ids['txt_origen_contactname'].text
        else:
            raise ValueError("Falta Contacto en DIRECCION ORIGEN")

        if fields.ids['txt_origen_corporatename'].text != "":
            data['origen_corporatename'] = fields.ids['txt_origen_corporatename'].text
        else:
            raise ValueError("Falta Empresa en DIRECCION ORIGEN")

        if fields.ids['txt_origen_neighborhood'].text != "":
            data['origen_neighborhood'] = fields.ids['txt_origen_neighborhood'].text

            if len(data['origen_neighborhood']) > 50:
                raise ValueError("Colonia en DIRECCION ORIGEN es mayor de 50")
        else:
            raise ValueError("Falta Colonia en DIRECCION ORIGEN")

        if fields.ids['txt_origen_phonenumber'].text != "":
            data['origen_phonenumber'] = fields.ids['txt_origen_phonenumber'].text

            if len(data['origen_phonenumber']) > 25:
                raise ValueError("Telefono en DIRECCION ORIGEN es mayor de 25")
        else:
            raise ValueError("Falta Telefono en DIRECCION ORIGEN")

        if fields.ids['txt_origen_state'].text != "":
            data['origen_state'] = fields.ids['txt_origen_state'].text

            if len(data['origen_state']) > 50:
                raise ValueError("Estado en DIRECCION ORIGEN es mayor de 50")
        else:
            raise ValueError("Falta Estado en DIRECCION ORIGEN")

        if fields.ids['txt_origen_zipcode'].text != "":
            data['origen_zipcode'] = fields.ids['txt_origen_zipcode'].text
        else:
            raise ValueError("Falta Zip Codigo en DIRECCION ORIGEN")

        data['origen_cellphone'] = fields.ids['txt_origen_cellphone'].text
        if len(data['origen_cellphone']) > 20:
            raise ValueError("Celular en DIRECCION ORIGEN es mayor de 20")

        return data

    def disable_DataOrigen(self):
        data = self.ids['label_container'].ids['origen_widget']
        data.ids['txt_origen_address1'].disabled = True
        data.ids['txt_origen_address2'].disabled = True
        data.ids['txt_origen_cellphone'].disabled = True
        data.ids['txt_origen_city'].disabled = True
        data.ids['txt_origen_contactname'].disabled = True
        data.ids['txt_origen_corporatename'].disabled = True
        data.ids['txt_origen_neighborhood'].disabled = True
        data.ids['txt_origen_phonenumber'].disabled = True
        data.ids['txt_origen_state'].disabled = True
        data.ids['txt_origen_zipcode'].disabled = True

    def enable_DataOrigen(self):
        data = self.ids['label_container'].ids['origen_widget']
        data.ids['txt_origen_address1'].disabled = False
        data.ids['txt_origen_address2'].disabled = False
        data.ids['txt_origen_cellphone'].disabled = False
        data.ids['txt_origen_city'].disabled = False
        data.ids['txt_origen_contactname'].disabled = False
        data.ids['txt_origen_corporatename'].disabled = False
        data.ids['txt_origen_neighborhood'].disabled = False
        data.ids['txt_origen_phonenumber'].disabled = False
        data.ids['txt_origen_state'].disabled = False
        data.ids['txt_origen_zipcode'].disabled = False

    def fill_DataDestino(self, _data):
        data = self.ids['label_container'].ids['destino_widget']
        data.ids['txt_destino_address1'].text = _data["address1"]
        data.ids['txt_destino_address2'].text = _data["address2"]
        data.ids['txt_destino_cellphone'].text = _data["cellphone"]
        data.ids['txt_destino_city'].text = _data['city']
        data.ids['txt_destino_contactname'].text = _data["contactname"]
        data.ids['txt_destino_corporatename'].text = _data["corporatename"]
        data.ids['txt_destino_customernumber'].text = _data['customernumber']
        data.ids['txt_destino_neighborhood'].text = _data['neighborhood']
        data.ids['txt_destino_phonenumber'].text = _data["phonenumber"]
        data.ids['txt_destino_state'].text = _data['state']
        data.ids['txt_destino_zipcode'].text = _data['zipcode']

    def clear_DataDestino(self):
        data = self.ids['label_container'].ids['destino_widget']
        data.ids['txt_destino_address1'].text = ""
        data.ids['txt_destino_address2'].text = ""
        data.ids['txt_destino_cellphone'].text = ""
        data.ids['txt_destino_city'].text = ""
        data.ids['txt_destino_contactname'].text = ""
        data.ids['txt_destino_corporatename'].text = ""
        data.ids['txt_destino_customernumber'].text = ""
        data.ids['txt_destino_neighborhood'].text = ""
        data.ids['txt_destino_phonenumber'].text = ""
        data.ids['txt_destino_state'].text = ""
        data.ids['txt_destino_zipcode'].text = ""

    def get_DataDestino(self):
        data = {}
        fields = self.ids['label_container'].ids['destino_widget']

        if fields.ids['txt_destino_address1'].text != "":
            data['destino_address1'] = fields.ids['txt_destino_address1'].text

            if len(data['destino_address1']) > 30:
                raise ValueError("Direccion 1 en DIRECCION DESTINO es mayor de 30")
        else:
            raise ValueError("Falta Direccion 1 en INFORMACION DESTINO")

        if fields.ids['txt_destino_address2'].text != "":
            data['destino_address2'] = fields.ids['txt_destino_address2'].text

            if len(data['destino_address2']) > 30:
                raise ValueError("Direccion 2 en DIRECCION DESTINO es mayor de 30")
        else:
            raise ValueError("Falta Direccion 2 en INFORMACION DESTINO")

        if fields.ids['txt_destino_city'].text != "":
            data['destino_city'] = fields.ids['txt_destino_city'].text

            if len(data['destino_city']) > 50:
                raise ValueError("Ciudad en DIRECCION DESTINO es mayor de 50")
        else:
            raise ValueError("Falta Ciudad en INFORMACION DESTINO")

        if fields.ids['txt_destino_contactname'].text != "":
            data['destino_contactname'] = fields.ids['txt_destino_contactname'].text
        else:
            raise ValueError("Falta Contacto en INFORMACION DESTINO")

        if fields.ids['txt_destino_corporatename'].text != "":
            data['destino_corporatename'] = fields.ids['txt_destino_corporatename'].text
        else:
            raise ValueError("Falta Empresa en INFORMACION DESTINO")

        if fields.ids['txt_destino_neighborhood'].text != "":
            data['destino_neighborhood'] = fields.ids['txt_destino_neighborhood'].text

            if len(data['destino_neighborhood']) > 50:
                raise ValueError("Colonia en DIRECCION DESTINO es mayor de 50")
        else:
            raise ValueError("Falta Colonia en INFORMACION DESTINO")

        if fields.ids['txt_destino_customernumber'].text != "":
            data['destino_customernumber'] = fields.ids['txt_destino_customernumber'].text
        else:
            raise ValueError("Falta Cliente en INFORMACION DESTINO")

        if fields.ids['txt_destino_phonenumber'].text != "":
            data['destino_phonenumber'] = fields.ids['txt_destino_phonenumber'].text

            if len(data['destino_phonenumber']) > 25:
                raise ValueError("Telefono en DIRECCION DESTINO es mayor de 25")
        else:
            raise ValueError("Falta Telefono en INFORMACION DESTINO")

        if fields.ids['txt_destino_state'].text != "":
            data['destino_state'] = fields.ids['txt_destino_state'].text

            if len(data['destino_state']) > 50:
                raise ValueError("Estado en DIRECCION DESTINO es mayor de 50")
        else:
            raise ValueError("Falta Estado en INFORMACION DESTINO")

        if fields.ids['txt_destino_zipcode'].text != "":
            data['destino_zipcode'] = fields.ids['txt_destino_zipcode'].text
        else:
            raise ValueError("Falta Zip Codigo en INFORMACION DESTINO")

        data['destino_address2'] = fields.ids['txt_destino_address2'].text
        if len(data['destino_address2']) > 30:
            raise ValueError("Direccion 2 en DIRECCION DESTINO es mayor de 30")

        data['destino_cellphone'] = fields.ids['txt_destino_cellphone'].text
        if len(data['destino_cellphone']) > 20:
            raise ValueError("Celular en DIRECCION DESTINO es mayor de 20")

        return data

    def disable_DataDestino(self):
        data = self.ids['label_container'].ids['destino_widget']
        data.ids['txt_destino_address1'].disabled = True
        data.ids['txt_destino_address2'].disabled = True
        data.ids['txt_destino_cellphone'].disabled = True
        data.ids['txt_destino_city'].disabled = True
        data.ids['txt_destino_contactname'].disabled = True
        data.ids['txt_destino_corporatename'].disabled = True
        data.ids['txt_destino_customernumber'].disabled = True
        data.ids['txt_destino_neighborhood'].disabled = True
        data.ids['txt_destino_phonenumber'].disabled = True
        data.ids['txt_destino_state'].disabled = True
        data.ids['txt_destino_zipcode'].disabled = True

    def enable_DataDestino(self):
        data = self.ids['label_container'].ids['destino_widget']
        data.ids['txt_destino_address1'].disabled = False
        data.ids['txt_destino_address2'].disabled = False
        data.ids['txt_destino_cellphone'].disabled = False
        data.ids['txt_destino_city'].disabled = False
        data.ids['txt_destino_contactname'].disabled = False
        data.ids['txt_destino_corporatename'].disabled = False
        data.ids['txt_destino_customernumber'].disabled = False
        data.ids['txt_destino_neighborhood'].disabled = False
        data.ids['txt_destino_phonenumber'].disabled = False
        data.ids['txt_destino_state'].disabled = False
        data.ids['txt_destino_zipcode'].disabled = False

    def fill_DataServicio(self, _data):
        data = self.ids['label_container'].ids['servicio_widget']
        data.ids['label_dir_destino'].text = _data["msg_dir_destino"]
        data.ids['txt_servicetypeid'].text = ""
        data.ids['txt_number_labels'].text = "1"
        data.ids['txt_contentdescription'].text = ""
        data.ids['txt_aditionalinfo'].text = _data['aditionalinfo']
        data.ids['txt_costcenter'].text = "0"
        data.ids['txt_content'].text = ""
        data.ids['txt_kilos'].text = ""
        data.ids['txt_servicetypeiddocret'].text = ""
        data.ids['txt_destino_countryid'].text = _data['destino_countryid']
        data.ids['txt_reference'].text = "."

    def clear_DataServicio(self):
        data = self.ids['label_container'].ids['servicio_widget']
        data.ids['txt_servicetypeid'].text = ""
        data.ids['txt_number_labels'].text = "1"

        data.ids['txt_contentdescription'].text = ""
        data.ids['txt_aditionalinfo'].text = ""
        data.ids['txt_costcenter'].text = "0"
        data.ids['txt_content'].text = ""
        data.ids['txt_kilos'].text = ""
        data.ids['txt_servicetypeiddocret'].text = ""
        data.ids['txt_destino_countryid'].text = ""
        data.ids['txt_reference'].text = "."
        data.ids['chk_deliverytoestafetaoffice'].active = False

    def get_DataServicio(self):
        data = {}

        fields = self.ids['label_container'].ids['servicio_widget']

        if fields.ids['txt_servicetypeid'].text == "Dia siguiente consumo facturacion mensual":
            data['servicetypeid'] = "60"
        elif fields.ids['txt_servicetypeid'].text == "Terrestre consumo facturacion mensual":
            data['servicetypeid'] = "70"
        elif fields.ids['txt_servicetypeid'].text == "Dos Dias consumo facturacion mensual":
            data['servicetypeid'] = "D0"
        else:
            raise ValueError("Falta Tipo Servicio en INFORMACION DE SERVICIO")

        if str(fields.ids['txt_number_labels'].text) != "":
            data['number_labels'] = str(fields.ids['txt_number_labels'].text)
        else:
            raise ValueError("Falta Cantidad Guias en INFORMACION DE SERVICIO")

        data['contentdescription'] = fields.ids['txt_contentdescription'].text
        data['aditionalinfo'] = fields.ids['txt_aditionalinfo'].text

        if fields.ids['txt_costcenter'].text != "":
            data['costcenter'] = fields.ids['txt_costcenter'].text
        else:
            raise ValueError("Falta Centro de Costo en INFORMACION DE SERVICIO")

        if fields.ids['txt_content'].text != "":
            data['content'] = fields.ids['txt_content'].text
        else:
            raise ValueError("Falta Contenido en INFORMACION DE SERVICIO")

        data['destino_countryid'] = fields.ids['txt_destino_countryid'].text

        if fields.ids['txt_reference'].text != "":
            data['reference'] = fields.ids['txt_reference'].text
        else:
            raise ValueError("Falta Referencia en INFORMACION DE SERVICIO")

        data['deliverytoestafetaoffice'] = str(fields.ids['chk_deliverytoestafetaoffice'].active)
        data['returndocument'] = str(fields.ids['chk_returndocument'].active)

        return data

    def disable_DataServicio(self):
        data = self.ids['label_container'].ids['servicio_widget']
        # data.ids['txt_servicetypeid'].disabled = True
        data.ids['txt_number_labels'].disabled = True

        data.ids['txt_contentdescription'].disabled = True
        data.ids['txt_aditionalinfo'].disabled = True
        data.ids['txt_costcenter'].disabled = True
        # data.ids['txt_content'].disabled = True
        data.ids['txt_kilos'].disabled = True
        data.ids['txt_servicetypeiddocret'].disabled = True
        data.ids['txt_destino_countryid'].disabled = True
        data.ids['txt_reference'].disabled = True
        data.ids['chk_deliverytoestafetaoffice'].disabled = True
        data.ids['chk_returndocument'].disabled = True

    def enable_DataServicio(self):
        data = self.ids['label_container'].ids['servicio_widget']
        # data.ids['txt_servicetypeid'].disabled = False
        data.ids['txt_number_labels'].disabled = False

        data.ids['txt_contentdescription'].disabled = False
        data.ids['txt_aditionalinfo'].disabled = False
        data.ids['txt_costcenter'].disabled = False
        # data.ids['txt_content'].disabled = False
        data.ids['txt_kilos'].disabled = False
        data.ids['txt_servicetypeiddocret'].disabled = False
        data.ids['txt_destino_countryid'].disabled = False
        data.ids['txt_reference'].disabled = False
        data.ids['chk_deliverytoestafetaoffice'].disabled = False
        data.ids['chk_returndocument'].disabled = False

    def clear_DataPaquete(self):
        data = self.ids['label_container'].ids['paquete_widget']
        data.ids['txt_peso'].text = ""
        data.ids['txt_kilos'].text = ""
        data.ids['txt_parcelTypeId'].text = ""
        data.ids['txt_largo'].text = ""
        data.ids['txt_alto'].text = ""
        data.ids['txt_ancho'].text = ""

    def get_DataPaquete(self):
        data = {}
        fields = self.ids['label_container'].ids['paquete_widget']

        if fields.ids['txt_peso'].text != "":
            data['peso'] = fields.ids['txt_peso'].text
        else:
            raise ValueError("Falta Peso en INFORMACION DEL PAQUETE")

        if fields.ids['txt_parcelTypeId'].text == "Sobre":
            data['parcelTypeId'] = "1"
        elif fields.ids['txt_parcelTypeId'].text == "Paquete":
            data['parcelTypeId'] = "4"
        else:
            raise ValueError("Falta Tipo de Empaque en INFORMACION DEL PAQUETE")

        return data

    def disable_DataPaquete(self):
        data = self.ids['label_container'].ids['paquete_widget']
        data.ids['txt_peso'].disabled = True
        data.ids['txt_kilos'].disabled = True
        # data.ids['txt_parcelTypeId'].disabled = True
        data.ids['txt_largo'].disabled = True
        data.ids['txt_alto'].disabled = True
        data.ids['txt_ancho'].disabled = True

    def enable_DataPaquete(self):
        data = self.ids['label_container'].ids['paquete_widget']
        data.ids['txt_peso'].disabled = False
        data.ids['txt_kilos'].disabled = False
        # data.ids['txt_parcelTypeId'].disabled = False
        data.ids['txt_largo'].disabled = False
        data.ids['txt_alto'].disabled = False
        data.ids['txt_ancho'].disabled = False

    def buscar_Factura(self):
        self._show_loader(True)

        self.factura_numero = str(self.ids['txt_factura_numero'].text)
        self.factura_tipo = self.ids['txt_factura_tipo'].text.upper()

        # fact = Factura.get(543, 'RI')
        if self.factura_numero != "" and self.factura_tipo != "":

            try:

                bandera, factura = Factura.get(self.factura_numero, self.factura_tipo)

                if bandera:
                    if len(factura) > 0:

                        bandera, pedido = DeliveryInst.get(factura[0].SDDOCO, factura[0].SDDCTO)

                        if bandera:
                            if len(pedido) > 0:

                                servicio = {}
                                servicio['aditionalinfo'] = "%s %s" % (
                                    self.factura_numero,
                                    self.factura_tipo
                                )

                                bandera, dir_origen = DireccionOrigen.get(self.factura_numero, self.factura_tipo)

                                self.clear_DataOrigen()
                                self.clear_DataDestino()
                                self.clear_DataServicio()
                                self.clear_DataPaquete()

                                if bandera:
                                    self.fill_DataOrigen(dir_origen)
                                    self.enable_DataOrigen()
                                else:
                                    self.failure(dir_origen['mensaje'])

                                bandera, dir_destino = DireccionDestino.get(self.factura_numero, self.factura_tipo)

                                if bandera:

                                    self.fill_DataDestino(dir_destino)
                                    self.enable_DataDestino()

                                    servicio['destino_countryid'] = dir_destino['Country']
                                    if pedido[0].SHDEL2 != "":
                                        servicio['msg_dir_destino'] = "(%s)  INFORMACION DEL SERVICIO" % (pedido[0].SHDEL2.strip())
                                    else:
                                        servicio['msg_dir_destino'] = "INFORMACION DEL SERVICIO"
                                    self.fill_DataServicio(servicio)
                                    self.enable_DataServicio()
                                    self.enable_DataPaquete()

                                else:
                                    self.failure(dir_destino['mensaje'])

                                bandera, etiquetas = Factura.ConsFactura(self.factura_numero, self.factura_tipo)

                                if bandera:
                                    if len(etiquetas):
                                        LabelsPopup(self, etiquetas, auto_dismiss=False).open()

                                self._show_loader(False)
                            else:
                            	self.failure("No se encontro Pedido")
                        else:
                            self.failure(pedido)

                    else:
            			self.failure("No se encontro factura")
            	else:
            		self.failure(factura)
            except Exception as e:
                self.failure(str(e))
        else:
            self.failure("Falto especificar Factura")

    def crear_Etiqueta(self):

        try:
            self._show_loader(True)

            usuario = ModeloUsuario.get(self.user_account)

            data_ambiente = {}

            if len(usuario) > 0:
                if usuario[0].profile.estafeta:
                    ambiente = usuario[0].profile.estafeta

                    data_ambiente['login'] = ambiente.login
                    data_ambiente['suscriber_id'] = ambiente.suscriber_id
                    data_ambiente['password'] = ambiente.password
                    data_ambiente['quadrant'] = str(ambiente.quadrant)
                    data_ambiente['tipo_papel'] = str(ambiente.paper_type)
                    data_ambiente['url'] = ambiente.url
                    data_ambiente['customer_number'] = ambiente.customer_number

                    data_ambiente['cot_url'] = ambiente.cot_url
                    data_ambiente['id_usuario'] = ambiente.cot_id_usuario
                    data_ambiente['usuario'] = ambiente.cot_usuario
                    data_ambiente['contra'] = ambiente.cot_contra

                    data_paquete = self.get_DataPaquete()
                    data_origen = self.get_DataOrigen()
                    data_origen['customer_number'] = data_ambiente['customer_number']
                    data_destino = self.get_DataDestino()

                    data_servicio = self.get_DataServicio()
                    data_servicio['peso'] = data_paquete['peso']
                    data_servicio['parcelTypeId'] = data_paquete['parcelTypeId']
                    data_servicio['customer_number'] = data_ambiente['customer_number']
                    data_servicio['cp_origen'] = data_origen['origen_zipcode']

                    if ambiente.office_num != "":
                        data_servicio['office_num'] = ambiente.office_num
                    else:
                        raise ValueError("Falta Oficina Numero en el ambiente configurado")

                    # Valida codigos
                    ws_cotizacion = CotizacionWS(data_ambiente["cot_url"])
                    ws_cotizacion.set_Credenciales(
                        data_ambiente['id_usuario'],
                        data_ambiente['usuario'],
                        data_ambiente['contra']
                    )
                    ws_cotizacion.set_EsFrecuencia("false")
                    ws_cotizacion.set_EsLista("true")
                    ws_cotizacion.set_TipoEnvio("false", "0", "0", "0", "0")
                    ws_cotizacion.set_Origen(data_origen['origen_zipcode'])
                    ws_cotizacion.set_Destino(data_destino['destino_zipcode'])

                    flag, results = ws_cotizacion.send(self.factura_numero, self.factura_tipo)

                    if flag:
                        # Crea Etiqueta
                        ws_create_label = CreateLabelWS(data_ambiente["url"])
                        ws_create_label.set_DireccionOrigen(data_origen)
                        ws_create_label.set_DireccionDestino(data_destino)
                        ws_create_label.set_DireccionAlternativa(data_destino)
                        ws_create_label.set_Servicio(data_servicio)
                        ws_create_label.set_Credenciales(data_ambiente)

                        flag, results, guide, archivo_pdf = ws_create_label.send(
                            self.factura_numero,
                            self.factura_tipo,
                            self.user_account
                        )

                        guias = guide.split('|')
                        for g in guias:
                            bandera, message = Factura.InsertaGuia(g, self.factura_numero, self.factura_tipo)

                        bandera, mensaje = Factura.ActualizaVtas(self.factura_numero, self.factura_tipo, guias[0])

                        if bandera:

                            pantalla_labelview = self.manager.get_screen('screen-labelview')
                            pantalla_labelview.archivo = archivo_pdf
                            pantalla_labelview.set_Label(flag, results, archivo_pdf)

                            self._show_loader(False)
                            self.clear_DataServicio()
                            self.clear_DataPaquete()
                            self.clear_DataOrigen()
                            self.clear_DataDestino()

                            self.disable_DataServicio()
                            self.disable_DataPaquete()
                            self.disable_DataOrigen()
                            self.disable_DataDestino()
                            self.activate_Control()
                            self.manager.current = 'screen-labelview'

                        else:
                            self.activate_Control()
                            self.failure(mensaje)

                    else:
                        self.activate_Control()
                        self.failure(results)
                else:
                    self.activate_Control()
                    self.failure("El usuario no tiene configurado un Ambiente")
            else:
                self.activate_Control()
                self.failure("No existe un usuario")

        except Exception as e:
            self.activate_Control()
            self.failure(str(e))

    def reimprimir_Etiqueta(self):

        try:
            self._show_loader(True)

            usuario = ModeloUsuario.get(self.user_account)

            data_ambiente = {}

            if len(usuario) > 0:
                if usuario[0].profile.estafeta:
                    ambiente = usuario[0].profile.estafeta

                    data_ambiente['quadrant'] = str(ambiente.quadrant)
                    data_ambiente['login'] = ambiente.login
                    data_ambiente['suscriber_id'] = ambiente.suscriber_id
                    data_ambiente['password'] = ambiente.password

                    data_ambiente['tipo_papel'] = str(ambiente.paper_type)
                    data_ambiente['url'] = ambiente.url
                    data_ambiente['customer_number'] = ambiente.customer_number

                    data_ambiente['cot_url'] = ambiente.cot_url
                    data_ambiente['id_usuario'] = ambiente.cot_id_usuario
                    data_ambiente['usuario'] = ambiente.cot_usuario
                    data_ambiente['contra'] = ambiente.cot_contra

                    data_paquete = self.get_DataPaquete()
                    data_origen = self.get_DataOrigen()
                    data_origen['customer_number'] = data_ambiente['customer_number']
                    data_destino = self.get_DataDestino()

                    data_servicio = self.get_DataServicio()
                    data_servicio['peso'] = data_paquete['peso']
                    data_servicio['parcelTypeId'] = data_paquete['parcelTypeId']
                    data_servicio['parcelNumber'] = self.guia
                    data_servicio['originZipCodeForRouting'] = data_origen['origen_zipcode']
                    # data_servicio['customer_number'] = data_ambiente['customer_number']
                    # data_servicio['cp_origen'] = data_origen['origen_zipcode']

                    # if ambiente.office_num != "":
                    #     data_servicio['office_num'] = ambiente.office_num
                    # else:
                    #     raise ValueError("Falta Oficina Numero en el ambiente configurado")

                    # Valida codigos
                    ws_cotizacion = CotizacionWS(data_ambiente["cot_url"])
                    ws_cotizacion.set_Credenciales(
                        data_ambiente['id_usuario'],
                        data_ambiente['usuario'],
                        data_ambiente['contra']
                    )
                    ws_cotizacion.set_EsFrecuencia("false")
                    ws_cotizacion.set_EsLista("true")
                    ws_cotizacion.set_TipoEnvio("false", "0", "0", "0", "0")
                    ws_cotizacion.set_Origen(data_origen['origen_zipcode'])
                    ws_cotizacion.set_Destino(data_destino['destino_zipcode'])

                    flag, results = ws_cotizacion.send(self.factura_numero, self.factura_tipo)

                    if flag:
                        # Crea Etiqueta
                        ws_reprint_label = ReprintLabelWS(data_ambiente["url"])
                        ws_reprint_label.set_DireccionOrigen(data_origen)
                        ws_reprint_label.set_DireccionDestino(data_destino)
                        # ws_reprint_label.set_DireccionAlternativa(data_destino)
                        ws_reprint_label.set_Servicio(data_servicio)
                        ws_reprint_label.set_Credenciales(data_ambiente)

                        flag, results, guide, archivo_pdf = ws_reprint_label.send(
                            self.factura_numero,
                            self.factura_tipo,
                            self.user_account
                        )

                        # guias = guide.split('|')
                        # for g in guias:
                        #     bandera, message = Factura.InsertaGuia(g, self.factura_numero, self.factura_tipo)

                        # bandera, mensaje = Factura.ActualizaVtas(self.factura_numero, self.factura_tipo, guias[0])

                        if flag:

                            pantalla_labelview = self.manager.get_screen('screen-labelview')
                            pantalla_labelview.archivo = archivo_pdf
                            pantalla_labelview.set_Label(flag, results, archivo_pdf)

                            self._show_loader(False)
                            self.clear_DataServicio()
                            self.clear_DataPaquete()
                            self.clear_DataOrigen()
                            self.clear_DataDestino()

                            self.disable_DataServicio()
                            self.disable_DataPaquete()
                            self.disable_DataOrigen()
                            self.disable_DataDestino()
                            self.activate_Control()
                            self.manager.current = 'screen-labelview'
                        else:
                            self.activate_Control()
                            self.failure(mensaje)

                    else:
                        self.activate_Control()
                        self.failure(results)
                else:
                    self.activate_Control()
                    self.failure("El usuario no tiene configurado un Ambiente")
            else:
                self.activate_Control()
                self.failure("No existe un usuario")

        except Exception as e:
            self.activate_Control()
            self.failure(str(e))

    def activate_Control(self):
        c_widget = self.ids['label_container'].ids['control_widget']
        c_widget.disabled = False


class DireccionesPopup(Popup):
    screen = ObjectProperty(None)
    padre = None

    def __init__(self, _screen, _padre, **kwargs):
        super(DireccionesPopup, self).__init__(**kwargs)
        self.screen = _screen
        self.padre = _padre
        # self.clear_Campo()

    def click_BotonBuscar(self):

        container = self.ids['container']
        container.clear_widgets()

        try:
            num_dir = self.ids['txt_direccion_numero'].text
            bandera, datos = NuevoDestino.get(int(num_dir))

            if bandera:
                opcion = DireccionOption(datos)
                container.add_widget(opcion)
            else:
                self.padre.failure(datos)
                self.dismiss()

        except Exception as e:
            self.padre.failure(str(e))
            self.dismiss()

    def click_BotonSeleccionar(self):
        datos = None

        for hijo in self.ids['container'].children:
            if hijo.ids['chk_option'].active is True:
                datos = hijo.registro

        if datos:
            self.padre.fill_DataDestino(datos)
            self.dismiss()


class DireccionOption(BoxLayout):
    registro = ObjectProperty(None)

    def __init__(self, _registro, **kwargs):
        super(DireccionOption, self).__init__(**kwargs)
        self.ids["lbl_option"].text = "%s - %s" % (
            _registro['corporatename'],
            _registro['address1'],
        )
        self.registro = _registro


class LabelsPopup(Popup):
    screen = ObjectProperty(None)

    def __init__(self, _screen, _records, **kwargs):
        super(LabelsPopup, self).__init__(**kwargs)
        self.screen = _screen
        self.load_Records(_records)

    def load_Records(self, _records):
        contenedor = self.ids['container']
        contenedor.clear_widgets()

        for registro in _records:
            widget = LabelOption(registro)
            contenedor.add_widget(widget)

    def click_BotonSeleccionar(self):
        value = ""

        for hijo in self.ids['container'].children:
            if hijo.ids['chk_option'].active is True:
                value = hijo.registro.TNVR03

        if value:
            window = self.get_root_window()
            screenmanager = window.children[1]
            pantalla = screenmanager.get_screen('screen-createlabel')
            pantalla.guia = value.strip()
            pantalla.is_reprint = True
            self.dismiss()

    def click_BotonSalir(self):
        # window = self.get_root_window()
        # screenmanager = window.children[1]
        # pantalla = screenmanager.get_screen('screen-createlabel')
        # pantalla.clear_DataOrigen()
        # pantalla.disable_DataOrigen()
        # pantalla.clear_DataDestino()
        # pantalla.disable_DataDestino()
        # pantalla.clear_DataServicio()
        # pantalla.disable_DataServicio()
        # pantalla.clear_DataPaquete()
        # pantalla.disable_DataPaquete()
        # pantalla.failure("No se puede generar Guias nuevas para esta Factura, debe reimprimir")
        self.dismiss()


class LabelOption(BoxLayout):
    registro = ObjectProperty(None)

    def __init__(self, _registro, **kwargs):
        super(LabelOption, self).__init__(**kwargs)
        self.ids["lbl_option"].text = _registro.TNVR03
        self.registro = _registro


class DestinoWidget(StackLayout):

    padre = None

    def click_BotonCambiarDireccion(self):

        padre = self.parent.parent.parent.parent.parent
        DireccionesPopup(self, padre).open()


class ServicioWidget(StackLayout):

    def open_TipoServicioPopup(self):
        TipoServicioPopup(self).open()

    def open_TipoContenidoPopup(self):
        ContenidoPopup(self).open()

    def fill_CampoContenido(self, _value):
        self.clear_CampoContenido()
        self.ids['txt_content'].text = _value

    def clear_CampoContenido(self):
        self.ids['txt_content'].text = ''

    def fill_CampoTipoServicio(self, _value):
        self.clear_CampoTipoServicio()
        self.ids['txt_servicetypeid'].text = _value

    def clear_CampoTipoServicio(self):
        self.ids['txt_servicetypeid'].text = ''


class TipoServicioPopup(Popup):
    padre = ObjectProperty(None)

    def __init__(self, padre, **kwargs):
        super(TipoServicioPopup, self).__init__(**kwargs)
        self.padre = padre

        self.show_All_Options()

    def show_All_Options(self):

        self.ids['container'].clear_widgets()

        widget10 = TipoServicioWidget("60", "Dia siguiente consumo facturacion mensual")
        widget70 = TipoServicioWidget("70", "Terrestre consumo facturacion mensual")
        widgetD0 = TipoServicioWidget("D0", "Dos Dias consumo facturacion mensual")

        self.ids['container'].add_widget(widget10)
        self.ids['container'].add_widget(widget70)
        self.ids['container'].add_widget(widgetD0)

    def click_SelectButton(self):

        value = ""

        for hijo in self.ids['container'].children:

            if hijo.ids['chk_tipo'].active is True:
                value = hijo.ids['lbl_tipo'].text

        if value:
            self.padre.fill_CampoTipoServicio(value)
            self.dismiss()


class TipoServicioWidget(BoxLayout):

    valor = ObjectProperty(None)

    def __init__(self, _valor, _descripcion, **kwargs):
        super(TipoServicioWidget, self).__init__(**kwargs)
        self.valor = _valor
        self.ids["lbl_tipo"].text = _descripcion


class ContenidoPopup(Popup):
    padre = ObjectProperty(None)

    def __init__(self, padre, **kwargs):
        super(ContenidoPopup, self).__init__(**kwargs)
        self.padre = padre

        self.show_All_Options()

    def show_All_Options(self):

        self.ids['container'].clear_widgets()

        widget_accesorio = ContenidoWidget("ACCESORIOS", "ACCESORIOS")
        widget_refacciones = ContenidoWidget("REFACCIONES", "REFACCIONES")

        self.ids['container'].add_widget(widget_accesorio)
        self.ids['container'].add_widget(widget_refacciones)

    def click_SelectButton(self):

        value = ""

        for hijo in self.ids['container'].children:

            if hijo.ids['chk_tipo'].active is True:
                value = hijo.valor

        if value:
            self.padre.fill_CampoContenido(value)
            self.dismiss()


class ContenidoWidget(BoxLayout):

    valor = ObjectProperty(None)

    def __init__(self, _valor, _descripcion, **kwargs):
        super(ContenidoWidget, self).__init__(**kwargs)
        self.valor = _valor
        self.ids["lbl_tipo"].text = _descripcion


class PaqueteWidget(StackLayout):

    def open_TipoPaquetePopup(self):
        TipoPaquetePopup(self).open()

    def fill_Campos(self, _value):

        self.clear_Campos()
        self.ids['txt_parcelTypeId'].text = _value

    def clear_Campos(self):
        self.ids['txt_parcelTypeId'].text = ''


class TipoPaquetePopup(Popup):
    padre = ObjectProperty(None)

    def __init__(self, padre, **kwargs):
        super(TipoPaquetePopup, self).__init__(**kwargs)
        self.padre = padre

        self.show_All_Options()

    def show_All_Options(self):

        self.ids['container'].clear_widgets()

        widgetSobre = TipoPaqueteWidget("1", "Sobre")
        widgetPaquete = TipoPaqueteWidget("4", "Paquete")

        self.ids['container'].add_widget(widgetSobre)
        self.ids['container'].add_widget(widgetPaquete)

    def click_SelectButton(self):

        value = ""

        for hijo in self.ids['container'].children:

            if hijo.ids['chk_tipo'].active is True:
                value = hijo.ids['lbl_tipo'].text

        if value:
            self.padre.fill_Campos(value)
            self.dismiss()


class TipoPaqueteWidget(BoxLayout):

    valor = ObjectProperty(None)

    def __init__(self, _valor, _descripcion, **kwargs):
        super(TipoPaqueteWidget, self).__init__(**kwargs)
        self.valor = _valor
        self.ids["lbl_tipo"].text = _descripcion


class ControlWidget(StackLayout):

    def click_BotonCrearEtiqueta(self):

        self.disabled = True

        screen_manager = self.get_root_window().children

        pantalla_crearetiqueta = screen_manager[0].get_screen('screen-createlabel')

        pantalla_crearetiqueta.crear_Etiqueta()

        # if pantalla_crearetiqueta.is_reprint:
        #     pantalla_crearetiqueta.reimprimir_Etiqueta()
        # else:
        #     pantalla_crearetiqueta.crear_Etiqueta()
