# import tempfile
import win32api
import win32print
import os
from libtools.filesystem import Archivo
from libtools.filesystem import Carpeta


class Printer(object):

    @classmethod
    def send(self, _archivo_pdf):

        # abspath = os.path.abspath(os.path.join(os.getcwd(), "etiquetas"))
        # folder = Carpeta(abspath)
        # file_name = "%s_%s.pdf" % (_factura_tipo, _factura_numero)
        # archivo = Archivo(folder, file_name)

        # print win32print.GetDefaultPrinter()
        _archivo_pdf.exist("buscando_pdf")
        filename = (_archivo_pdf.get_Abspath())
        win32api.ShellExecute(
            0,
            "print",
            filename,
            #
            # If this is None, the default printer will
            # be used anyway.
            #
            '/d:"%s"' % win32print.GetDefaultPrinter(),
            ".",
            0
        )
