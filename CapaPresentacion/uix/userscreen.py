# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from CapaNegocio.gestordb import ModeloUsuario
from CapaNegocio.gestordb import ModeloEstafetaAmbiente


class UserScreen(Screen):

    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        self._show_loader(False)
        self.show_Registros()

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

    def show_Registros(self):
        try:
            self._show_loader(True)
            contenedor = self.ids['user_container'].ids['container']
            contenedor.clear_widgets()
            registros = ModeloUsuario.get()

            for registro in registros:
                widget = UsuarioItem(registro)
                contenedor.add_widget(widget)

            self._show_loader(False)

        except Exception as e:
            self.failure(str(e))

    def click_BotonBuscar(self):
        self.show_Registros()

    def click_BotonNuevo(self):
        UserAddPopup().open()


class UsuarioItem(StackLayout):

    registro = ObjectProperty(None)

    def __init__(self, _registro, **kwargs):
        super(UsuarioItem, self).__init__(**kwargs)

        self.ids['lbl_cuenta'].text = _registro.username

        if _registro.get_full_name() == '':
            self.ids['lbl_descripcion'].text = "Sin descripcion"
        else:
            self.ids['lbl_descripcion'].text = _registro.get_full_name()

        self.ids['lbl_date'].text = _registro.date_joined.strftime('%m/%d/%Y')

        self.registro = _registro

    def click_BotonEditar(self):
        UserEditPopup(self.registro).open()


class UserAddPopup(Popup):

    def click_BotonCrear(self):
        clave = self.ids['txt_cuenta'].text
        nombre = self.ids['txt_nombre'].text
        descripcion = self.ids['txt_apellidos'].text
        contrasena = self.ids['txt_password'].text
        estafeta_cuenta_clave = self.ids['txt_estafeta_cuenta'].text
        ModeloUsuario.add(clave, nombre, descripcion, contrasena, estafeta_cuenta_clave)
        self.dismiss()

    def click_BotonEstafetaAmbientes(self):
        EstafetaAmbientesPopup(self).open()


class UserEditPopup(Popup):

    def __init__(self, _registro, **kwargs):
        super(UserEditPopup, self).__init__(**kwargs)
        self.ids['txt_cuenta'].text = _registro.username
        self.ids['txt_nombre'].text = _registro.first_name
        self.ids['txt_apellidos'].text = _registro.last_name
        self.ids['chk_activo'].active = _registro.is_active

    def click_BotonGuardar(self):
        clave = self.ids['txt_cuenta'].text
        nombre = self.ids['txt_nombre'].text
        descripcion = self.ids['txt_apellidos'].text
        contrasena = self.ids['txt_password'].text
        activo = self.ids['chk_activo'].active
        estafeta_cuenta_clave = self.ids['txt_estafeta_cuenta'].text
        ModeloUsuario.edit(clave, nombre, descripcion, contrasena, activo, estafeta_cuenta_clave)

        self.dismiss()

    def click_BotonEstafetaAmbientes(self):
        EstafetaAmbientesPopup(self).open()


class EstafetaAmbientesPopup(Popup):
    screen = ObjectProperty(None)

    def __init__(self, _screen, **kwargs):
        super(EstafetaAmbientesPopup, self).__init__(**kwargs)
        self.screen = _screen
        self.load_Records()

    def load_Records(self):
        contenedor = self.ids['container']
        contenedor.clear_widgets()
        registros = ModeloEstafetaAmbiente.get()

        for registro in registros:
            widget = EstafetaAmbienteOption(registro)
            contenedor.add_widget(widget)

    def click_SelectButton(self):
        value = ""

        for hijo in self.ids['container'].children:
            if hijo.ids['chk_cuenta_estafeta'].active is True:
                value = hijo.registro.clave

        if value:
            self.screen.ids['txt_estafeta_cuenta'].text = value
            self.dismiss()


class EstafetaAmbienteOption(BoxLayout):
    registro = ObjectProperty(None)

    def __init__(self, _registro, **kwargs):
        super(EstafetaAmbienteOption, self).__init__(**kwargs)
        self.ids["lbl_cuenta_estafeta"].text = _registro.clave
        self.registro = _registro
