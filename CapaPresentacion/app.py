import os.path
from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '720')
Config.set('kivy', 'exit_on_escape', '0')
from kivy.app import App

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition

from CapaPresentacion.uix.loginscreen import LoginScreen
from CapaPresentacion.uix.createlabelscreen import CreateLabelScreen
from CapaPresentacion.uix.userscreen import UserScreen
from CapaPresentacion.uix.estafetascreen import EstafetaScreen
from CapaPresentacion.uix.ideascreen import IdeaScreen

from CapaNegocio.gestordb import ModeloUsuario
from CapaNegocio.estafeta import EstafetaWebService

from CapaPresentacion.idea import IdeaCollection

import configparser
import threading
import jsonpickle
import simplecrypt

'''
The App implementation
'''


class SegretoApp(App):

    def build(self):
        self.icon = 'data/icon/idealogo.png'  # Don't know why icon isn't set :(
        self.title = 'EmbApp380'
        self.init()
        return self.screenmanager

    def init(self):
        self.username = ''
        self.password = ''
        self.crypt_file_path = ''
        self.screenmanager = ScreenManager(transition=SwapTransition())

        self.loginscreen = LoginScreen(name='screen-login')
        self.loginscreen.bind(on_login=self.login)

        self.userscreen = UserScreen(name='screen-user')

        self.createlabelscreen = CreateLabelScreen(name='screen-createlabel')

        self.estafetascreen = EstafetaScreen(name='screen-estafeta')

        self.ideascreen = IdeaScreen(name='screen-idea')
        # self.ideascreen.bind(on_quit_app=self.quit)
        # self.ideascreen.bind(on_Users=self.goto_Users)

        self.screenmanager.add_widget(self.loginscreen)
        self.screenmanager.add_widget(self.userscreen)
        self.screenmanager.add_widget(self.createlabelscreen)
        self.screenmanager.add_widget(self.estafetascreen)

        self.screenmanager.add_widget(self.ideascreen)

        self.screenmanager.current = 'screen-login'
        # self.screenmanager.current = 'screen-createlabel'

    def encrypt_store_data(self, crypt_file_path, password, idea_collection):
        self.screenmanager.clear_widgets()
        ser_data = jsonpickle.encode(idea_collection)
        enc_data = simplecrypt.encrypt(password, ser_data)
        with open(crypt_file_path, 'wb') as f:
            f.write(enc_data)
        self.stop()

    def login(self, *args):
        self.username = self.loginscreen.ids['grid'].username
        self.password = self.loginscreen.ids['grid'].password

        if ModeloUsuario.login(self.username, self.password):
            self.screenmanager.current = 'screen-createlabel'
        else:
            self.loginscreen.login_failure('Usuario o Contrasena no valida')
            self.username = ''
            self.password = ''

        # uname = self.loginscreen.ids['grid'].username
        # paswd = self.loginscreen.ids['grid'].password
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

    def goto_Usuarios(self):
        self.screenmanager.current = "screen-user"

    def goto_Etiquetas(self):
        self.screenmanager.current = "screen-createlabel"

    def goto_EstafetaCuentas(self):
        self.screenmanager.current = "screen-estafeta"

    def decrypt_data(self, crypt_data, password):
        try:
            dec_data = simplecrypt.decrypt(password, crypt_data)
            self.password = password
            self.idea_collection = jsonpickle.decode(dec_data.decode('utf8'))
            self.ideascreen.set_idea_collection(self.idea_collection)
            self.screenmanager.current = 'screen-idea'
        except simplecrypt.DecryptionException:
            self.loginscreen.login_failure('Password error')
            self.username = ''
            self.password = ''
            self.crypt_file_path = ''

    def start_decrypt_thread(self, crypt_data, paswd):
        t = threading.Thread(target=self.decrypt_data,
                             args=(crypt_data, paswd))
        t.daemon = True
        t.start()

    def start_encrypt_thread(self, crypt_file_path, password, idea_collection):
        t = threading.Thread(target=self.encrypt_store_data, args=(
            crypt_file_path, password, idea_collection))
        t.daemon = True
        t.start()

    def quit(self, *args):
        idea_collection = self.ideascreen.idea_collection
        self.start_encrypt_thread(
            self.crypt_file_path, self.password, idea_collection)

    def on_pause(self):
        return True

    def crear_Etiqueta(self):

        # Datos de Servicio:
        service_fields = self.createlabelscreen.ids['label_container'].ids['servicio_widget'].ids

        num_cliente = service_fields['txt_num_cliente'].text
        servicetypeid = service_fields['txt_servicetypeid'].text
        number_labels = str(service_fields['txt_number_labels'].text)
        office_num = service_fields['txt_office_num'].text
        contentdescription = service_fields['txt_contentdescription'].text
        aditionalinfo = service_fields['txt_aditionalinfo'].text
        costcenter = service_fields['txt_costcenter'].text
        content = service_fields['txt_content'].text
        # kilos = service_fields['txt_kilos'].text
        destino_countryid = service_fields['txt_destino_countryid'].text
        reference = service_fields['txt_reference'].text

        deliverytoestafetaoffice = str(service_fields['chk_deliverytoestafetaoffice'].active)
        returndocument = str(service_fields['chk_returndocument'].active)

        # Datos de Conexion:
        credentials_fields = self.createlabelscreen.ids['label_container'].ids['credenciales_widget'].ids

        login = credentials_fields['txt_login'].text
        suscriber_id = credentials_fields['txt_suscriber_id'].text
        password = credentials_fields['txt_password'].text
        quadrant = credentials_fields['txt_quadrant'].text
        tipo_papel = credentials_fields['txt_tipo_papel'].text
        url = credentials_fields['txt_url'].text

        ws = EstafetaWebService(url)

        ws.set_Servicio(
            num_cliente,
            "",
            "",
            "",
            number_labels,
            office_num,
            aditionalinfo,
            content,
            contentdescription,
            costcenter,
            deliverytoestafetaoffice,
            destino_countryid,
            "",
            "",
            reference,
            returndocument,
            servicetypeid,
            ""
        )
        ws.set_Credenciales(login, tipo_papel, password, quadrant, suscriber_id)

        print ws.create_Label()
