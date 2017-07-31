import os

from libtools.filesystem import Archivo
from libtools.filesystem import Carpeta

from kivy.uix.screenmanager import Screen
from CapaNegocio.printing import Printer


class LabelViewScreen(Screen):

    fac_numero = None
    fac_tipo = None

    def __init__(self, **kwargs):
        super(LabelViewScreen, self).__init__(**kwargs)

    def imprimir(self):
        Printer.send(self.fac_numero, self.fac_tipo)

    def set_Label(self, _text):

        abspath = os.path.abspath(os.path.join(os.getcwd(), "etiquetas"))
        folder = Carpeta(abspath)
        file_name = "%s_%s.png" % (self.fac_tipo, self.fac_numero)
        archivo = Archivo(folder, file_name)
        self.ids['label_container'].ids['labelview_widget'].ids['img_etiqueta'].source = ""

        try:
            archivo.exist("buscando_imagen")
            self.ids['label_container'].ids['labelview_widget'].ids['img_etiqueta'].source = archivo.get_Abspath()
        except Exception:
            deafult_abspath = os.path.abspath(os.path.join(os.getcwd(), "data", "images", "no_img.png"))
            self.ids['label_container'].ids['labelview_widget'].ids['img_etiqueta'].source = deafult_abspath

        self.ids['label_container'].ids['labelview_widget'].ids['lbl_etiqueta_view'].text = _text
