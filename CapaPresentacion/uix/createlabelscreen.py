# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
# from CapaPresentacion.uix.widget import Toast
from CapaNegocio.gestordb import ModeloEstafetaAmbiente
# from CapaNegocio.gestordb import Factura
from CapaNegocio.gestordb import DireccionOrigen
from CapaNegocio.gestordb import DireccionDestino
from CapaNegocio.gestordb import ModeloUsuario

from CapaNegocio.estafeta import CreateLabelWS
from CapaNegocio.estafeta import CotizacionWS


class CreateLabelScreen(Screen):

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

    def fill_DataAmbiente(self, _user_account):
        self.user_account = _user_account
        usuario = ModeloUsuario.get(self.user_account)

        if len(usuario) > 0:
            if usuario[0].profile.estafeta:

                ambiente = usuario[0].profile.estafeta
                data = self.ids['label_container'].ids['estafeta_ambiente_widget']
                data.ids['txt_cuenta'].text = ambiente.clave
                data.ids['txt_url'].text = ambiente.url
                data.ids['txt_login'].text = ambiente.login
                data.ids['txt_suscriber_id'].text = ambiente.suscriber_id
                data.ids['txt_password'].text = ambiente.password
                data.ids['txt_quadrant'].text = str(ambiente.quadrant)
                data.ids['txt_tipo_papel'].text = str(ambiente.paper_type)
                data.ids['txt_customernumber'].text = ambiente.customer_number

                data.ids['txt_cot_url'].text = ambiente.cot_url
                data.ids['txt_cot_id_usuario'].text = ambiente.cot_id_usuario
                data.ids['txt_cot_usuario'].text = ambiente.cot_usuario
                data.ids['txt_cot_contra'].text = ambiente.cot_contra

            else:
                self.failure("El usuario no tiene configurado un Ambiente")
        else:
            self.failure("No existe un usuario")

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

    def fill_DataServicio(self, _data):
        data = self.ids['label_container'].ids['servicio_widget']
        data.ids['txt_servicetypeid'].text = "70"
        data.ids['txt_number_labels'].text = "1"
        data.ids['txt_office_num'].text = "130"
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
        data.ids['txt_servicetypeid'].text = "70"
        data.ids['txt_number_labels'].text = "1"
        data.ids['txt_office_num'].text = "130"
        data.ids['txt_contentdescription'].text = ""
        data.ids['txt_aditionalinfo'].text = ""
        data.ids['txt_costcenter'].text = "0"
        data.ids['txt_content'].text = ""
        data.ids['txt_kilos'].text = ""
        data.ids['txt_servicetypeiddocret'].text = ""
        data.ids['txt_destino_countryid'].text = ""
        data.ids['txt_reference'].text = "."
        data.ids['chk_deliverytoestafetaoffice'].active = False

    def clear_DataPaquete(self):
        data = self.ids['label_container'].ids['paquete_widget']
        data.ids['txt_peso'].text = ""
        data.ids['txt_kilos'].text = ""
        data.ids['txt_parcelTypeId'].text = "1"
        data.ids['txt_largo'].text = ""
        data.ids['txt_alto'].text = ""
        data.ids['txt_ancho'].text = ""

    def get_DataPaquete(self):
        data = {}
        fields = self.ids['label_container'].ids['paquete_widget']
        data['peso'] = fields.ids['txt_peso'].text
        data['parcelTypeId'] = fields.ids['txt_parcelTypeId'].text

        # data['kilos'] = pack_fields['txt_kilos'].text
        # data['largo'] = pack_fields['txt_largo'].text
        # data['alto'] = pack_fields['txt_alto'].text
        # data['ancho'] = pack_fields['txt_ancho'].text
        return data

    def get_DataOrigen(self):
        data = {}
        fields = self.ids['label_container'].ids['origen_widget']
        data['origen_address1'] = fields.ids['txt_origen_address1'].text
        data['origen_address2'] = fields.ids['txt_origen_address2'].text
        data['origen_cellphone'] = fields.ids['txt_origen_cellphone'].text
        data['origen_city'] = fields.ids['txt_origen_city'].text
        data['origen_contactname'] = fields.ids['txt_origen_contactname'].text
        data['origen_corporatename'] = fields.ids['txt_origen_corporatename'].text
        data['origen_neighborhood'] = fields.ids['txt_origen_neighborhood'].text
        data['origen_phonenumber'] = fields.ids['txt_origen_phonenumber'].text
        data['origen_state'] = fields.ids['txt_origen_state'].text
        data['origen_zipcode'] = fields.ids['txt_origen_zipcode'].text

        return data

    def get_DataDestino(self):
        data = {}
        fields = self.ids['label_container'].ids['destino_widget']
        data['destino_address1'] = fields.ids['txt_destino_address1'].text
        data['destino_address2'] = fields.ids['txt_destino_address2'].text
        data['destino_cellphone'] = fields.ids['txt_destino_cellphone'].text
        data['destino_city'] = fields.ids['txt_destino_city'].text
        data['destino_contactname'] = fields.ids['txt_destino_contactname'].text
        data['destino_corporatename'] = fields.ids['txt_destino_corporatename'].text
        data['destino_neighborhood'] = fields.ids['txt_destino_neighborhood'].text
        data['destino_customernumber'] = fields.ids['txt_destino_customernumber'].text
        data['destino_phonenumber'] = fields.ids['txt_destino_phonenumber'].text
        data['destino_state'] = fields.ids['txt_destino_state'].text
        data['destino_zipcode'] = fields.ids['txt_destino_zipcode'].text

        return data

    def get_DataServicio(self):
        data = {}

        fields = self.ids['label_container'].ids['servicio_widget']
        data['servicetypeid'] = fields.ids['txt_servicetypeid'].text
        data['number_labels'] = str(fields.ids['txt_number_labels'].text)
        data['office_num'] = fields.ids['txt_office_num'].text
        data['contentdescription'] = fields.ids['txt_contentdescription'].text
        data['aditionalinfo'] = fields.ids['txt_aditionalinfo'].text
        data['costcenter'] = fields.ids['txt_costcenter'].text
        data['content'] = fields.ids['txt_content'].text
        data['destino_countryid'] = fields.ids['txt_destino_countryid'].text
        data['reference'] = fields.ids['txt_reference'].text
        data['deliverytoestafetaoffice'] = str(fields.ids['chk_deliverytoestafetaoffice'].active)
        data['returndocument'] = str(fields.ids['chk_returndocument'].active)

        return data

    def get_DataAmbiente(self):
        data = {}

        fields = self.ids['label_container'].ids['estafeta_ambiente_widget']
        data['login'] = fields.ids['txt_login'].text
        data['suscriber_id'] = fields.ids['txt_suscriber_id'].text
        data['password'] = fields.ids['txt_password'].text
        data['quadrant'] = fields.ids['txt_quadrant'].text
        data['tipo_papel'] = fields.ids['txt_tipo_papel'].text
        data['url'] = fields.ids['txt_url'].text
        data['customer_number'] = fields.ids['txt_customernumber'].text

        data['cot_url'] = fields.ids['txt_cot_url'].text
        data['id_usuario'] = fields.ids['txt_cot_id_usuario'].text
        data['usuario'] = fields.ids['txt_cot_usuario'].text
        data['contra'] = fields.ids['txt_cot_contra'].text

        return data

    def buscar_Factura(self):
        self._show_loader(True)

        self.factura_numero = str(self.ids['txt_factura_numero'].text)
        self.factura_tipo = self.ids['txt_factura_tipo'].text

        self.clear_DataOrigen()
        self.clear_DataDestino()
        self.clear_DataServicio()
        self.clear_DataPaquete()

        # fact = Factura.get(543, 'RI')
        if self.factura_numero != "" and self.factura_tipo != "":

            servicio = {}
            servicio['aditionalinfo'] = "%s %s" % (
                self.factura_numero,
                self.factura_tipo
            )

            bandera, dir_origen = DireccionOrigen.get(self.factura_numero, self.factura_tipo)

            if bandera:
                self.fill_DataOrigen(dir_origen)
            else:
                self.failure(dir_origen['mensaje'])

            bandera, dir_destino = DireccionDestino.get(self.factura_numero, self.factura_tipo)

            if bandera:
                self.fill_DataDestino(dir_destino)

                servicio['destino_countryid'] = dir_destino['Country']
                self.fill_DataServicio(servicio)
            else:
                self.failure(dir_destino['mensaje'])

            self._show_loader(False)
        else:
            self.failure("Falto especificar Factura")

    def crear_Etiqueta(self):
        try:
            self._show_loader(True)

            data_paquete = self.get_DataPaquete()
            data_ambiente = self.get_DataAmbiente()
            data_origen = self.get_DataOrigen()
            data_origen['customer_number'] = data_ambiente['customer_number']
            data_destino = self.get_DataDestino()

            data_servicio = self.get_DataServicio()
            data_servicio['peso'] = data_paquete['peso']
            data_servicio['parcelTypeId'] = data_paquete['parcelTypeId']
            data_servicio['customer_number'] = data_ambiente['customer_number']
            data_servicio['cp_origen'] = data_origen['origen_zipcode']

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

            import ipdb; ipdb.set_trace()
            if flag:
                # Crea Etiqueta
                ws_create_label = CreateLabelWS(data_ambiente["url"])
                ws_create_label.set_DireccionOrigen(data_origen)
                ws_create_label.set_DireccionDestino(data_destino)
                ws_create_label.set_DireccionAlternativa(data_destino)
                ws_create_label.set_Servicio(data_servicio)
                ws_create_label.set_Credenciales(data_ambiente)

                flag, results, guide = ws_create_label.send(
                    self.factura_numero,
                    self.factura_tipo,
                    self.user_account
                )

                self.manager.get_screen('screen-labelview').fac_numero = self.factura_numero
                self.manager.get_screen('screen-labelview').fac_tipo = self.factura_tipo
                self.manager.get_screen('screen-labelview').set_Label(flag, results)

                self._show_loader(False)
                self.manager.current = 'screen-labelview'

            else:
                self.failure(results)

        except Exception as e:
            self.failure(str(e))


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

        widget10 = TipoServicioWidget("60", "Día siguiente consumo facturación mensual")
        widget70 = TipoServicioWidget("70", "Terrestre consumo facturación mensual")

        self.ids['container'].add_widget(widget10)
        self.ids['container'].add_widget(widget70)

    def click_SelectButton(self):

        value = ""

        for hijo in self.ids['container'].children:

            if hijo.ids['chk_tipo'].active is True:
                value = hijo.valor

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
                value = hijo.valor

        if value:
            self.padre.fill_Campos(value)
            self.dismiss()


class TipoPaqueteWidget(BoxLayout):

    valor = ObjectProperty(None)

    def __init__(self, _valor, _descripcion, **kwargs):
        super(TipoPaqueteWidget, self).__init__(**kwargs)
        self.valor = _valor
        self.ids["lbl_tipo"].text = _descripcion


class EstafetaAmbienteWidget(StackLayout):

    def click_BotonEstafetaAmbientes(self):
        EstafetaAmbientesPopup(self).open()

    def fill_Campos(self, ambiente):

        self.clear_Campos()
        self.ids['txt_cuenta'].text = ambiente.clave
        self.ids['txt_url'].text = ambiente.url
        self.ids['txt_login'].text = ambiente.login
        self.ids['txt_suscriber_id'].text = ambiente.suscriber_id
        self.ids['txt_password'].text = ambiente.password
        self.ids['txt_quadrant'].text = str(ambiente.quadrant)
        self.ids['txt_tipo_papel'].text = str(ambiente.paper_type)
        self.ids['txt_customernumber'].text = ambiente.customer_number

        self.ids['txt_cot_url'].text = ambiente.cot_url
        self.ids['txt_cot_id_usuario'].text = ambiente.cot_id_usuario
        self.ids['txt_cot_usuario'].text = ambiente.cot_usuario
        self.ids['txt_cot_contra'].text = ambiente.cot_contra

    def clear_Campos(self):
        self.ids['txt_cuenta'].text = ''
        self.ids['txt_url'].text = ''
        self.ids['txt_login'].text = ''
        self.ids['txt_suscriber_id'].text = ''
        self.ids['txt_password'].text = ''
        self.ids['txt_quadrant'].text = ''
        self.ids['txt_tipo_papel'].text = ''
        self.ids['txt_customernumber'].text = ''

        self.ids['txt_cot_url'].text = ""
        self.ids['txt_cot_id_usuario'].text = ""
        self.ids['txt_cot_usuario'].text = ""
        self.ids['txt_cot_contra'].text = ""


class EstafetaAmbientesPopup(Popup):
    padre = ObjectProperty(None)

    def __init__(self, _padre, **kwargs):
        super(EstafetaAmbientesPopup, self).__init__(**kwargs)
        self.padre = _padre
        self.load_Records()

    def load_Records(self):
        contenedor = self.ids['container']
        contenedor.clear_widgets()
        registros = ModeloEstafetaAmbiente.get_Actives()

        for registro in registros:
            widget = EstafetaAmbienteOption(registro)
            contenedor.add_widget(widget)

    def click_BotonSeleccionar(self):
        value = ""

        for hijo in self.ids['container'].children:
            if hijo.ids['chk_cuenta_estafeta'].active is True:
                value = hijo.registro

        if value:
            self.padre.fill_Campos(value)
            self.dismiss()


class EstafetaAmbienteOption(BoxLayout):
    registro = ObjectProperty(None)

    def __init__(self, _registro, **kwargs):
        super(EstafetaAmbienteOption, self).__init__(**kwargs)
        self.ids["lbl_cuenta_estafeta"].text = _registro.clave
        self.registro = _registro


class ControlWidget(StackLayout):

    def click_BotonCrearEtiqueta(self):
        screen_manager = self.get_root_window().children
        screen_manager[0].get_screen('screen-createlabel').crear_Etiqueta()
