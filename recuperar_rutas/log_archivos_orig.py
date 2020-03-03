

from tkinter.filedialog import askdirectory, asksaveasfile

from openpyxl import Workbook

from modelos.archivos_pdf_xml import ArchivosOrig
from modelos.log import Log


class Log_Archivos_Orig(Log):
    """Crea Log de la carpeta especificado de los archivos"""

    def __init__(self, ruta):

        self.ruta = ruta

        archivo = ArchivosOrig(self.ruta)
        self.rutas_pdf = archivo.depurar_rutas()
       
        
        self.hoja_titulo = "Archivos PDF"
        Log.__init__(self, self.hoja_titulo)


    def escribir_rutas_pdf(self):
        """llama la clase log que lee y escribe rutas de los
        recibos de Nomina o Listados"""


        print("--Escribiendo rutas de RECIBOS...")

        hoja_activa = 0
        columna_inicial = 1
        fila = 1

        datos = self.separar_datos(self.rutas_pdf[0])

        titulos = ["AÑO-PERIODO", "NOMINA", "ARCHIVO", "RUTA"]
        lista   = [datos[0], datos[1], datos[2], datos[3]]

        

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
        datos = self.separar_datos(self.rutas_pdf[1])
        titulos  = ["AÑO-PERIODO", "NOMINA", "ARCHIVO", "RUTA"]
        lista   = [datos[0], datos[1], datos[2], datos[3]]

        self.escribir_titulo(titulos, fila, hoja_activa)
        self.escribir_en_hoja(lista, columna_inicial, hoja_activa)

        
        
        

    def ejecutar(self, ruta_save):
        self.escribir_rutas_pdf()
        self.escribir_rutas_xml()
        
        self.guardar_archivo_log(ruta_save)


    def separar_datos(self, lista):
        año    = list()
        nomina = list()
        archivo = list()
        ruta   = list()

        for datos in lista:
             
            
            
            año.append(datos[0][0])
            nomina.append(datos[1][0])                
            archivo.append(datos[2][0])
            ruta.append(datos[3][0])
            
            
           

        return año, nomina, archivo, ruta







        
log = Log_Archivos_Orig(askdirectory())
log.ejecutar(asksaveasfile())