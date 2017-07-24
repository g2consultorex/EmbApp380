

from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout

from gestordb import ModelProfile


class UserScreen(Screen):

    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        # self.show_All_Users()

    def show_All_Users(self):

        self.ids['user_container'].ids['container'].clear_widgets()

        usuarios = ModelProfile.get()

        for usuario in usuarios:
            widget = UsuarioWidget(usuario)
            self.ids['user_container'].ids['container'].add_widget(widget)

    def open_AddPopup(self):
        UserAddPopup().open()

    def add_UsuarioWidget(self):
        widget = UsuarioWidget()
        self.ids['user_container'].ids['container'].add_widget(widget)


class UsuarioWidget(StackLayout):

    def __init__(self, usuario, **kwargs):
        super(UsuarioWidget, self).__init__(**kwargs)

        self.ids['lbl_cuenta'].text = usuario.username

        if usuario.get_full_name() == '':
            self.ids['lbl_descripcion'].text = "Sin descripcion"
        else:
            self.ids['lbl_descripcion'].text = usuario.get_full_name()

        self.ids['lbl_date'].text = usuario.date_joined.strftime('%m/%d/%Y')


class UserAddPopup(Popup):

    def click_CreateButton(self):
        clave = self.ids['lbl_cuenta'].text
        nombre = self.ids['lbl_nombre'].text
        descripcion = self.ids['lbl_apellidos'].text

        ModelProfile.add(clave, nombre, descripcion)

        self.dismiss()
