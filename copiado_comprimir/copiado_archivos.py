

from copiado_comprimir.modelos.archivos import Archivo




class CopiadoArchivos:

    def __init__(self, archivo_excel):

        self.copiado = Archivo(archivo_excel)
    
    def ejecutar(self, ruta_destino):
        hojas = ['Archivos PDF', 'Timbres_XML']

        self.copiado.copiar_archivos(hojas[0], ruta_destino)
        print("RECIBOS COPIADOS")

        self.copiado.copiar_archivos(hojas[1], ruta_destino)
        print("TIMBRES COPIADOS")





       

