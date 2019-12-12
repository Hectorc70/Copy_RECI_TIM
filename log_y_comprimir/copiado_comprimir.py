import os
import os.path

from tkinter.filedialog import askdirectory
#from tkinter.filedialog import askdirectory

import zipfile

from log_y_comprimir.modelos.log_respaldo import Log_Destino 


class Rutas():   

    def recuperar_carpetas(self, ruta):
        """Recupera las Rutas de Archivos PDF y XML"""

        self.ruta             = ruta 
        self.carpetas_nominas = dict()
        self.carpeta_base     = dict()  
       
         


        for ruta, carpetas, documentos in os.walk(self.ruta):                    
            
             
            for archivo in documentos:     
                print(archivo)            
                extencion_archivo = os.path.splitext(archivo)

                if extencion_archivo == '.pdf' or extencion_archivo == '.xml':
                
                    tipo_nomina = ruta.split('\\')[2]
                    periodo     = ruta.split('\\')[1]
                    nom_periodo = periodo + "-" + tipo_nomina
                    ruta_nom    = ruta.split('\\')[0] + "\\" + periodo + "\\" + tipo_nomina         #ruta de carpeta de cada nomina                    
                    
                    self.carpeta_base["CARPETA_BASE"] = ruta.split('\\')[0] + ruta.split('\\')[1]
                    
                    self.carpetas_nominas[nom_periodo] = ruta_nom.replace('/','\\')
                else:
                    continue


        return  self.carpetas_nominas 
                  



class ArchivoCopiado(Rutas):

    
    def __init__(self, carpeta_lectura): 
        self.carpeta_lectura = carpeta_lectura

        Rutas.__init__(self)
        self.recuperar_carpetas(self.carpeta_lectura)

        self.ruta = carpeta_lectura         
        
    def escribir_info_log(self):  
        """Escribe un log por cada carpeta(Tipo de Nomina)"""  
        
      

        for ruta_nom in self.carpetas_nominas.values():
            print(ruta_nom)
          
            log = Log_Destino(ruta_nom)
            log.escribir_rutas_pdf()
            log.escribir_rutas_xml()


            ruta_guardado = ruta_nom + "\\" + "Log.xlsx" 
            log.guardar(ruta_guardado)
            

    def comprimir(self):
        carpeta_zip  = self.carpeta_base["CARPETA_BASE"] + "\\" + "COMPRIMIDOS"
        for carpeta in self.carpetas_nominas.values():
            
            print(archivo)
            comprimir = zipfile.ZipFile(carpeta_zip, 'w')
            comprimir.write(archivo, compress_type=zipfile.ZIP_DEFLATED)
 
        comprimir.close()
        pass










    
               
                
            
                   




    




       

