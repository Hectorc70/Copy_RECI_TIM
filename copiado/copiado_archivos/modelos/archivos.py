
from os import makedirs
import os.path as path 
from tkinter.filedialog import askopenfile

from shutil import copy

from archivo_excel import Archivo_excel
from compresion import ArchivoComprimido





    
  

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
        


        COLUMNA = 'A'
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



        hoja_lectura = self.hojas_nombres[hoja]

        self.rutas_archivos_destino = list()
        self.rutas_destino_carpetas = list()

        self.ruta_madre             = list()
        self.nomina_destino         = dict()
        self.carpetas_nom_archivos       = dict()
        listas_rutas_destino        = list()


        columna = 'C'
        fila_i  = 1                                             #Fila que omite al leer

        titulos = hoja_lectura[columna]

        for titulo in range(fila_i,len(titulos)):            
            
            listas_rutas_destino.append([titulos[titulo].value])

        
        for lista_ruta in  listas_rutas_destino:

            for ruta in lista_ruta:
                ruta_div = ruta.split('\\')
                disco    = ruta_div[0]
                carpeta  = ruta_div[1]
                periodo  = ruta_div[2]
                nomina   = ruta_div[3]
                 
                nomina_per  =  nomina + "-" + periodo  
                ruta_nomina =  disco + "\\" + carpeta + "\\" + periodo + "\\" + nomina + "\\"

                ruta_div.pop()
                ruta_carpeta = "\\".join(ruta_div)
               
                

                self.rutas_archivos_destino.append(ruta)                
                self.rutas_destino_carpetas.append(ruta_carpeta)

                self.ruta_madre.append(disco + "\\" + carpeta+"\\")
                self.nomina_destino[nomina_per] = ruta_nomina
                
                self.carpetas_nom_archivos[nomina_per]=[lista_ruta]
        
            
        
        




                   

    

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


    
        

       

    def comprimir_archivos(self):
        self.extraer_rutas_originales('Archivos PDF')
        self.extraer_rutas_destino('Archivos PDF')

        for ruta_carpeta in self.carpetas_nom_archivos:
            print(ruta_carpeta)
           
            comprimido = ArchivoComprimido(ruta_carpeta)
            comprimido.comprimir()
        
        


        
       
archivo = Archivo(askopenfile())
archivo.comprimir_archivos()
       

               









        
    

    
