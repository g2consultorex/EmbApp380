from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from CapaNegocio.gestordb import ModeloEstafetaUser


class CreateLabelScreen(Screen):

    def __init__(self, **kwargs):
        super(CreateLabelScreen, self).__init__(**kwargs)


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



class CredencialesWidget(StackLayout):

    def open_CredencialesPopup(self):
        CredencialesPopup(self).open()

    def fill_Campos(self, cuenta):

        self.clear_Campos()
        self.ids['txt_cuenta'].text = cuenta.clave
        self.ids['txt_login'].text = cuenta.login
        self.ids['txt_suscriber_id'].text = cuenta.suscriber_id
        self.ids['txt_password'].text = cuenta.password
        self.ids['txt_quadrant'].text = str(cuenta.quadrant)
        self.ids['txt_tipo_papel'].text = str(cuenta.paper_type)

    def clear_Campos(self):
        self.ids['txt_cuenta'].text = ''
        self.ids['txt_login'].text = ''
        self.ids['txt_suscriber_id'].text = ''
        self.ids['txt_password'].text = ''
        self.ids['txt_quadrant'].text = ''
        self.ids['txt_tipo_papel'].text = ''


class CredencialesPopup(Popup):

    padre = ObjectProperty(None)

    def __init__(self, padre, **kwargs):

        super(CredencialesPopup, self).__init__(**kwargs)

        self.padre = padre

        self.show_All_Cuentas()

    def show_All_Cuentas(self):

        self.ids['container'].clear_widgets()

        cuentas = ModeloEstafetaUser.get()

        for cuenta in cuentas:
            widget = CuentaWidget(cuenta)
            self.ids['container'].add_widget(widget)

    def click_SelectButton(self):

        cuenta = None

        for hijo in self.ids['container'].children:

            if hijo.ids['chk_cuenta'].active is True:
                cuenta = hijo.cuenta

        if cuenta:
            self.padre.fill_Campos(cuenta)
            self.dismiss()


class CuentaWidget(BoxLayout):

    cuenta = ObjectProperty(None)

    def __init__(self, _cuenta, **kwargs):
        super(CuentaWidget, self).__init__(**kwargs)
        self.ids["lbl_cuenta"].text = _cuenta.clave
        self.cuenta = _cuenta
