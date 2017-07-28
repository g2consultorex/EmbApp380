from kivy.uix.screenmanager import Screen


class LabelViewScreen(Screen):

    def __init__(self, **kwargs):
        super(LabelViewScreen, self).__init__(**kwargs)

    def set_Label(self, _text):
        self.ids['label_container'].ids['labelview_widget'].ids['lbl_etiqueta_view'].text = _text
