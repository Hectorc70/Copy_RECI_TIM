import os
import os.path
from tkinter.filedialog import askdirectory

class Rutas():   

    def recuperar_carpetas(self, ruta):
        """Recupera las Rutas de Archivos PDF y XML"""

        self.ruta = ruta 
        self.carpetas_nominas = dict()  
   
         


        for ruta, carpetas, documentos in os.walk(self.ruta):                    
            

            for archivo in documentos:     
                print(archivo)            
                
                
                tipo_nomina = ruta.split('\\')[2]
                periodo     = ruta.split('\\')[1]
                nom_periodo = periodo + "-" + tipo_nomina
                ruta_nom    = ruta.split('\\')[0] + "\\" + periodo + "\\" + tipo_nomina         #ruta de carpeta de cada nomina                    
                 
                self.carpetas_nominas[nom_periodo] = ruta_nom.replace('/','\\')
                
        return  self.carpetas_nominas 
                  
            
                
                                                      
                    
      
    
    








                
               

                        




        


