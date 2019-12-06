


from openpyxl import Workbook

from originales.modelos.rutas import Rutas 
from originales.modelos.log import Log


class Log_Archivos_Orig(Log, Rutas):
    """Crea Log de la carpeta especificado de los archivos"""

    def __init__(self, ruta):
        self.ruta_carpeta = ruta
        Rutas.__init__(self, self.ruta_carpeta)
               


        
        self.hoja_titulo = "Archivos PDF"
        Log.__init__(self, self.hoja_titulo)


    def escribir_rutas_pdf(self):
        """llama la clase log que lee y escribe rutas de los
        recibos de Nomina o Listados"""


        print("--Escribiendo rutas de RECIBOS...")

        hoja_activa = 0
        columna_inicial = 1
        fila = 1

        
        titulos = ["Rutas_PDF", "Año-Periodo", "Ruta Destino"]
        lista   = [self.recibos_pdf, self.periodo, self.recibos_pdf_destino]

        

        self.escribir_titulo(titulos, fila, hoja_activa)
        self.escribir_en_hoja(lista, columna_inicial, hoja_activa)
       

        
            

    def escribir_rutas_xml(self):
        """llama la clase log que lee y escribe rutas de los
        timbres de las Nominas"""  

        print("--Escribiendo rutas de TIMBRES...")

        hoja_activa = 1
        columna_inicial = 1
        fila = 1

        self.crear_hoja_nueva("Timbres_XML")
        self.hoja_activa = 2
        titulos  = ["Rutas_XML", "Año-Periodo", "Ruta Destino"]
        lista   = [self.timbres,self.periodo_timbres, self.ruta_destino_timbres]

        self.escribir_titulo(titulos, fila, hoja_activa)
        self.escribir_en_hoja(lista, columna_inicial, hoja_activa)
        
        

    def ejecutar(self, ruta_save):
        self.escribir_rutas_pdf()
        self.escribir_rutas_xml()
        
        self.guardar_archivo_log(ruta_save)







        

