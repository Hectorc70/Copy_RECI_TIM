
from os import makedirs
import os.path as path 
#from tkinter.filedialog import askopenfile

from shutil import copy

from copiado.modelos.archivo_excel import Archivo_excel
from copiado.modelos.rutas import unir_cadenas






    
  

class Archivo(Archivo_excel):
    """Clase Archivo que mueve o copia archivos"""

    def __init__(self, ruta):
        Archivo_excel.__init__(self, ruta)
        
        
  


    def extraer_rutas_originales(self,hoja):        
        """"Extrae las rutas de los archivos originales
            almacenadas de la pestaña
            que se requiera(Debe ser el nombre de la hoja)
            del log"""

        
        hoja_lectura = self.hojas_nombres[hoja]

        rutas_archivo_original = list()       
        listas_rutas_orig      = list()
        


        COLUMNA = 'D'
        fila_i  = 1                                     #Fila que omite en leer

        titulos = hoja_lectura[COLUMNA]
       

        
        for titulo in range(fila_i,len(titulos)):
            
            listas_rutas_orig.append([titulos[titulo].value])
        

        for lista_ruta in  listas_rutas_orig:
            for ruta in lista_ruta:
                rutas_archivo_original.append(ruta)

        return rutas_archivo_original
    

        

       
    def extraer_rutas_destino(self, hoja, ruta_base):
        """"Extrae las rutas de destino 
            almacenadas de la pestaña
            que se requiera(Debe ser el nombre  de la hoja)
            del log"""


        hoja_lectura = self.hojas_nombres[hoja]

        rutas_destino          = list()       
        listas_rutas__destino  = list()
        rutas_carpetas = list()

        COLUMNA = 'E'
        fila_i  = 1                                     #Fila que omite en leer

        titulos = hoja_lectura[COLUMNA]

        
        for titulo in range(fila_i,len(titulos)):
            
            listas_rutas__destino.append([titulos[titulo].value])
        

        for lista_ruta in  listas_rutas__destino:
            for ruta in lista_ruta:

                rutas_destino_completa = self.armar_ruta_destino(ruta_base, ruta)
                rutas_destino.append(rutas_destino_completa[0])
                rutas_carpetas.append(rutas_destino_completa[1])
        
        return rutas_destino, rutas_carpetas               

    

    def copiar_archivos(self, hoja, ruta_destino_base):
        """"Extrae las rutas almacenadas 
            de la pestaña de XML del log"""

        self.hoja = hoja

        rutas_orig    = self.extraer_rutas_originales(self.hoja)
        rutas_destino = self.extraer_rutas_destino(self.hoja, ruta_destino_base)        
        
        

        for ruta_original, ruta_destino, ruta_carpeta in zip(rutas_orig,
                                                             rutas_destino[0],
                                                             rutas_destino[1]):

            if path.exists(ruta_destino):                                   #VALIDA si el archivo existe
              continue
            
            else: 
                try:                                                            #Excepcion solo cuando no existe la carpeta la crea
                    copy(ruta_original, ruta_destino)
                    print("Archivo Copiado: " + ruta_destino)

                except FileNotFoundError:
                    print("Creando RUTA: " + ruta_carpeta)
                    
                    makedirs( ruta_carpeta, exist_ok=True)
                    copy(ruta_original, ruta_destino)      

                
    


    def armar_ruta_destino(self, ruta_base, ruta):
        """Arma la ruta de destino"""

        ruta_split = ruta.split('\\')
        
       
        ruta_base_split = ruta_base.split('\\')
        ruta_base_split_r = ruta_base_split[::-1]

        for ruta in ruta_base_split_r:
            ruta_split.insert(0, ruta)

        ruta_destino_completa = unir_cadenas('\\', ruta_split)
        ruta_split.pop(-1)
        ruta_destino_carpeta = unir_cadenas('\\', ruta_split)
        
        
        return [ruta_destino_completa, ruta_destino_carpeta]


          


    
        
#archivo = Archivo(askopenfile())
#archivo.copiar_archivos('Archivos PDF', 'C:\\Pruebas_cfdi')

        


               









        
    

    
