import os
import os.path

from tkinter.filedialog import askdirectory
#from tkinter.filedialog import askdirectory



from log_y_comprimir.modelos.log_respaldo import Log_Destino
from log_y_comprimir.modelos.archivo_comprimir import ArchivoComprimido  


class ArchivoCopiado():

    
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

            a_comprimido = ArchivoComprimido(ruta_nom)
            
            print("Archivos Comprimidos")

            ruta_guardado = ruta_nom + "\\" + "Log.xlsx" 
            log.guardar(ruta_guardado)
            

    #def comprimir(self):
        
        #carpeta_zip  = self.carpeta_base["CARPETA_BASE"] + "\\" + "COMPRIMIDOS"
        
        
            
            
            
            
 
        #comprimir.close()
    










    
               
                
            
                   




    




       

