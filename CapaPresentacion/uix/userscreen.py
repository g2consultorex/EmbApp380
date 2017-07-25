# -*- coding: utf-8 -*-


from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty

from CapaNegocio.gestordb import ModeloUsuario


class UserScreen(Screen):

    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        self.show_All_Users()

    def show_All_Users(self):

        self.ids['user_container'].ids['container'].clear_widgets()

        usuarios = ModeloUsuario.get()

        for usuario in usuarios:
            widget = UsuarioWidget(usuario)
            self.ids['user_container'].ids['container'].add_widget(widget)

    def open_AddPopup(self):
        UserAddPopup().open()

    def add_UsuarioWidget(self):
        widget = UsuarioWidget()
        self.ids['user_container'].ids['container'].add_widget(widget)


class UsuarioWidget(StackLayout):

    user = ObjectProperty(None)

    def __init__(self, usuario, **kwargs):
        super(UsuarioWidget, self).__init__(**kwargs)

        self.ids['lbl_cuenta'].text = usuario.username

        if usuario.get_full_name() == '':
            self.ids['lbl_descripcion'].text = "Sin descripcion"
        else:
            self.ids['lbl_descripcion'].text = usuario.get_full_name()

        self.ids['lbl_date'].text = usuario.date_joined.strftime('%m/%d/%Y')

        self.user = usuario

    def click_BotonEditar(self):
        UserEditPopup(self.user).open()


class UserAddPopup(Popup):

    def click_CreateButton(self):

        clave = self.ids['txt_cuenta'].text
        nombre = self.ids['txt_nombre'].text
        descripcion = self.ids['txt_apellidos'].text
        contrasena = self.ids['txt_password'].text

        ModeloUsuario.add(clave, nombre, descripcion, contrasena)

        self.dismiss()


class UserEditPopup(Popup):

    def __init__(self, _usuario, **kwargs):
        super(UserEditPopup, self).__init__(**kwargs)

        self.ids['txt_cuenta'].text = _usuario.username
        self.ids['txt_nombre'].text = _usuario.first_name
        self.ids['txt_apellidos'].text = _usuario.last_name
        self.ids['chk_activo'].active = _usuario.is_active

    def click_SaveButton(self):

        clave = self.ids['txt_cuenta'].text
        nombre = self.ids['txt_nombre'].text
        descripcion = self.ids['txt_apellidos'].text
        contrasena = self.ids['txt_password'].text
        activo = self.ids['chk_activo'].active
        ModeloUsuario.edit(clave, nombre, descripcion, contrasena, activo)

        self.dismiss()
