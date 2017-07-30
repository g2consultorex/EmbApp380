from kivy.uix.screenmanager import Screen

# from kivy.cache import Cache
# from kivy.logger import Logger
# from kivy.core.image import ImageLoaderBase, ImageData, ImageLoader
#
# from kivy.graphics.texture import Texture
# Debug = False
#
# import io
# from pyPdf import PdfFileWriter, PdfFileReader
# import PythonMagick as pm
# import pygame


class LabelViewScreen(Screen):

    def __init__(self, **kwargs):
        super(LabelViewScreen, self).__init__(**kwargs)

    def set_Label(self, _text):
        self.ids['label_container'].ids['labelview_widget'].ids['img_etiqueta'].source = 'etiquetas/ZE_102466.png'
        self.ids['label_container'].ids['labelview_widget'].ids['lbl_etiqueta_view'].text = _text
