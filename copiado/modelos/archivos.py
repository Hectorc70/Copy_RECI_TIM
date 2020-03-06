
from os import makedirs
import os.path as path 
from tkinter.filedialog import askopenfile

from shutil import copy

from copiado.modelos.archivo_excel import Archivo_excel






    
  

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

        self.rutas_archivo_original = list()       
        listas_rutas_orig           = list()
        


        COLUMNA = 'D'
        fila_i  = 1                                     #Fila que omite en leer

        titulos = hoja_lectura[COLUMNA]
       

        
        for titulo in range(fila_i,len(titulos)):
            
            listas_rutas_orig.append([titulos[titulo].value])
        

        for lista_ruta in  listas_rutas_orig:
            for ruta in lista_ruta:
                self.rutas_archivo_original.append(ruta)
    

        

       
    def extraer_rutas_destino(self, hoja):
        """"Extrae las rutas de destino 
            almacenadas de la pestaña
            que se requiera(Debe ser el nombre  de la hoja)
            del log"""



            
        
            
        
        




                   

    

    def copiar_archivos(self, hoja):
        """"Extrae las rutas almacenadas 
            de la pestaña de XML del log"""

        self.hoja = hoja

        self.extraer_rutas_originales(self.hoja)
        self.extraer_rutas_destino(self.hoja)  
        
        
        

        for ruta_original, ruta_destino, ruta_carpeta in zip(self.rutas_archivo_original,
                                                             self.rutas_archivos_destino,
                                                             self.rutas_destino_carpetas):

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
                
                    print("Archivo Copiado: "  + ruta_destino)


          

       
    
        


        


               









        
    

    
