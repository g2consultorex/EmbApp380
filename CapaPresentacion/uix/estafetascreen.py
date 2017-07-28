# -*- coding: utf-8 -*-


from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty

from CapaNegocio.gestordb import ModeloEstafetaUser


class EstafetaScreen(Screen):

    def __init__(self, **kwargs):
        super(EstafetaScreen, self).__init__(**kwargs)
        self.show_All_Records()

    def show_All_Records(self):

        self.ids['estafeta_container'].ids['container'].clear_widgets()

        records = ModeloEstafetaUser.get()

        for registro in records:
            widget = EstafetaWidget(registro)
            self.ids['estafeta_container'].ids['container'].add_widget(widget)

    def open_AddPopup(self):
        EstafetaAddPopup().open()

    def add_RecordWidget(self):
        widget = EstafetaWidget()
        self.ids['estafeta_container'].ids['container'].add_widget(widget)


class EstafetaWidget(StackLayout):

    estafeta_user = ObjectProperty(None)

    def __init__(self, _registro, **kwargs):
        super(EstafetaWidget, self).__init__(**kwargs)

        self.ids['lbl_clave'].text = _registro.clave
        self.ids['lbl_login'].text = _registro.login
        self.ids['lbl_date'].text = _registro.created_date.strftime('%m/%d/%Y')

        self.estafeta_user = _registro

    def click_BotonEditar(self):
        EstafetaEditPopup(self.estafeta_user).open()


class EstafetaAddPopup(Popup):

    def click_CreateButton(self):

        clave = self.ids['txt_clave'].text
        url = self.ids['txt_url'].text
        login = self.ids['txt_login'].text
        password = self.ids['txt_password'].text
        quadrant = self.ids['txt_quadrant'].text
        suscriber_id = self.ids['txt_suscriber_id'].text
        paper_type = self.ids['txt_paper_type'].text
        es_principal = self.ids['chk_es_principal'].active

        ModeloEstafetaUser.add(clave, url, login, password, quadrant, suscriber_id, paper_type, es_principal)

        self.dismiss()


class EstafetaEditPopup(Popup):

    def __init__(self, _registro, **kwargs):
        super(EstafetaEditPopup, self).__init__(**kwargs)

        self.ids['txt_clave'].text = _registro.clave
        self.ids['txt_url'].text = _registro.url
        self.ids['txt_login'].text = _registro.login
        self.ids['txt_password'].text = _registro.password
        self.ids['txt_quadrant'].text = str(_registro.quadrant)
        self.ids['txt_suscriber_id'].text = _registro.suscriber_id
        self.ids['txt_paper_type'].text = str(_registro.paper_type)
        self.ids['chk_es_principal'].active = _registro.es_principal

    def click_SaveButton(self):

        clave = self.ids['txt_clave'].text
        url = self.ids['txt_url'].text
        login = self.ids['txt_login'].text
        password = self.ids['txt_password'].text
        quadrant = self.ids['txt_quadrant'].text
        suscriber_id = self.ids['txt_suscriber_id'].text
        paper_type = self.ids['txt_paper_type'].text
        es_principal = self.ids['chk_es_principal'].active

        ModeloEstafetaUser.edit(clave, url, login, password, quadrant, suscriber_id, paper_type, es_principal)

        self.dismiss()
