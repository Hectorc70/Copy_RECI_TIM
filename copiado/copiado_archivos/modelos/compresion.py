
import os
#from tkinter.filedialog import askdirectory

import zipfile







class ArchivoComprimido():

    def __init__(self, carpetas):
        self.carpetas = carpetas    




    def comprimir(self):

        
        for carpeta in self.carpetas:
            for archivo in carpeta:
                print(archivo)
                comprimir = zipfile.ZipFile(archivo, 'w')
                comprimir.write(archivo, compress_type=zipfile.ZIP_DEFLATED)
 
        comprimir.close()

               
                
            
                   






