from kivy.uix.screenmanager import Screen
from kivy.uix.stacklayout import StackLayout
from gestordb import ModelProfile


class UserScreen(Screen):

    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        self.show_All_Users()

    def show_All_Users(self):
        usuarios = ModelProfile.get()

        for usuario in usuarios:
            widget = UsuarioWidget()
            self.ids['user_container'].ids['container'].add_widget(widget)

    def add_UsuarioWidget(self):

        widget = UsuarioWidget()
        self.ids['user_container'].ids['container'].add_widget(widget)


class UsuarioWidget(StackLayout):
    pass
