from tkinter.filedialog import asksaveasfile, askdirectory, askopenfile, askopenfilename

from originales.log_archivos_orig import Log_Archivos_Orig
from copiado.copiado_archivos import copiar_archivos
from log_y_comprimir.copiado_comprimir import ArchivoCopiado




def recuperar_rutas_orig():
    
    log = Log_Archivos_Orig(askdirectory())
    log.ejecutar(asksaveasfile())


def ejecutar_copiado_de_archivos(ruta):
    copiar_archivos(ruta)


#crear log por nomina y comprimir
   
#def crear_log(ruta):
    
    #log = ArchivoCopiado(ruta)
    #log.escribir_info_log()
    #log.comprimir()



#recuperar_rutas_orig()
ejecutar_copiado_de_archivos(askopenfile())
#crear_log(askdirectory())

