import os
import os.path

import zipfile



class ArchivoComprimido:
    """Clase Modelo que comprime una carpeta(Nomina)"""
    def __init__(self, carpeta):
        self.carpeta   = carpeta
       

        self.comprimir()
    def obtener_archivos(self):
        """Obtiene archivos de cada carpeta(nomina)"""

        self.archivos = list()
        self.carpeta_base = dict()

        for ruta, carpetas, archivos in os.walk(self.carpeta):
            for archivo in archivos:

                extencion_archivo = os.path.splitext(archivo)
                ruta_archivo = ruta + "\\" + archivo

                if extencion_archivo[-1] == ".pdf" or extencion_archivo[-1] == ".xml":
                    self.carpeta_base["CARPETA_BASE"] = ruta.split('\\')[0] + "\\" + ruta.split('\\')[1]
                    self.archivos.append(ruta_archivo)
                




    def comprimir(self):
        self.obtener_archivos()

        ruta_completa =  self.carpeta_base["CARPETA_BASE"] + "\\" + "COMPRIMIDOS.zip" 
        for archivo in self.archivos:  

            periodo = archivo.split("\\")[2]
            ruta_completa =  self.carpeta_base["CARPETA_BASE"] + "\\" + periodo + "\\" + "COMPRIMIDOS.zip" 
            
            comprimir = zipfile.ZipFile(ruta_completa, 'w')
            comprimir.write(archivo, compress_type=zipfile.ZIP_DEFLATED)
        


