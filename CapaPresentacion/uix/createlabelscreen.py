from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from CapaNegocio.gestordb import ModeloEstafetaUser


class CreateLabelScreen(Screen):

    def __init__(self, **kwargs):
        super(CreateLabelScreen, self).__init__(**kwargs)


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

    def __init__(self, padre,**kwargs):

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
            
            if hijo.ids['chk_cuenta'].active == True:
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
