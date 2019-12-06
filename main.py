from tkinter.filedialog import asksaveasfile, askdirectory, askopenfile

from originales.log_archivos_orig import Log_Archivos_Orig
from copiado.log.log_nomina import Log_pdf_xml
from copiado.copiado_archivos.copiado_archivos import copiar_archivos





def recuperar_rutas_orig():
    
    log = Log_Archivos_Orig(askdirectory())
    log.ejecutar(asksaveasfile())


def ejecutar_copiado_de_archivos(ruta):
    copiar_archivos(ruta)


def crear_log(ruta):
    
    log = Log_pdf_xml(ruta)
    log.escribir_info_log()




crear_log(askdirectory())

