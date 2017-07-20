# import os.path
from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
Config.set('kivy', 'exit_on_escape', '0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition
from esconnect.uix.loginscreen import LoginScreen

import configparser
# import threading
# import jsonpickle
# import simplecrypt
'''
The App implementation
'''


class EsconnectApp(App):

    def build(self):
        self.icon = 'data/icon/segreto_icon.png'  # Don't know why icon isn't set :(
        self.title = 'EmbApp380'
        self.init()
        return self.screenmanager

    def init(self):
        # Inicializa Passwords
        self.username = ''
        self.password = ''

        # self.crypt_file_path = ''
        # Crea Administrador de ventanas
        self.screenmanager = ScreenManager(transition=SwapTransition())
        self.loginscreen = LoginScreen(name='screen-login')

        # Agrega evento login
        self.loginscreen.bind(on_login=self.login)

        # self.ideascreen = IdeaScreen(name='screen-idea')
        # self.ideascreen.bind(on_quit_app=self.quit)
        self.screenmanager.add_widget(self.loginscreen)
        # self.screenmanager.add_widget(self.ideascreen)

        # Establece Login como pantalla principal
        self.screenmanager.current = 'screen-login'

    def login(self, *args):
        print "Entro a login"
        self.username = self.loginscreen.ids['grid'].username
        self.password = self.loginscreen.ids['grid'].password

        # config = configparser.ConfigParser()
        # config.read('settings.ini')
        # for section in config.sections():
        #     username = config.get(section, 'username')
        #     if username == uname:
        #         self.crypt_file_path = config.get(section, 'file')
        #         self.username = uname
        #         with open(self.crypt_file_path, 'ab+') as f:
        #             f.seek(0)
        #             crypt_data = f.read()
        #             if crypt_data == b'':
        #                 self.password = paswd
        #                 self.screenmanager.current = 'screen-idea'
        #             else:
        #                 self.start_decrypt_thread(crypt_data, paswd)
        # if self.username == '':
        #     self.loginscreen.login_failure('User not found')
        #     self.username = ''
        #     self.password = ''
        #     self.crypt_file_path = ''

    def quit(self, *args):
        pass
        # idea_collection = self.ideascreen.idea_collection
        # self.start_encrypt_thread(
        #     self.crypt_file_path, self.password, idea_collection)

    def on_pause(self):
        return True
