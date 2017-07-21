# -*- coding: utf-8 -*-


from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from esconnect.uix.widget import Toast
from kivy.clock import Clock


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self._show_loader(False)
        self.register_event_type('on_login')

    def _show_toast(self, text):
        self.ids['toast'].show(text)

    def _show_loader(self, show):
        if show:
            self.ids['loader'].opacity = 1.0
        else:
            self.ids['loader'].opacity = 0.0

    def try_login(self):
        print "Entro a Try_login"
        self._show_loader(True)
        self.ids['grid'].disabled = True
        if self.ids['grid'].username == '':
            self.login_failure('Especifica una Cuenta')
        elif self.ids['grid'].password == '':
            self.login_failure('Especifica una Contraseña')
        else:
            self.dispatch('on_login')

    def login_failure(self, error):
        self._show_toast(error)
        self.ids['grid'].disabled = False
        self._show_loader(False)

    def on_login(self):
        pass


class LoginGrid(BoxLayout):
    # pass
    username = ''
    password = ''

    def __init__(self, **kwargs):
        super(LoginGrid, self).__init__(**kwargs)
        self.register_event_type('on_login')

    def on_password(self, value):
        self.password = value
        # if len(value) > len(self.password):
        #     if not u"\u2022" in value[-1:]:
        #         self.password += value[-1:]
        # elif len(value) < len(self.password):
        #     self.password = self.password[:(len(value) - len(self.password))]
        # else:
        #     return
        # self.ids['inp_password'].text = len(self.password) * u"\u2022"

    def on_username(self, value):
        self.username = value

    def on_disabled(self, instance, disabled):
        super(LoginGrid, self).on_disabled(instance, disabled)
        if disabled:
            self.ids['inp_username'].hint_text = self.username
            self.ids['inp_password'].hint_text = self.password
            # self.ids['inp_password'].hint_text = len(self.password) * u"\u2022"
        else:
            self.ids['inp_username'].hint_text = 'Cuenta'
            self.ids['inp_password'].hint_text = 'Contraseña'

    def on_login(self):
        pass
