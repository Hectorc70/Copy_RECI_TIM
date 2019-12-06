import os
import os.path
from tkinter.filedialog import askdirectory

class Rutas():
       

    def recuperar_rutas_archivos(self, ruta):
        """Recupera las Rutas de Archivos PDF y XML"""

        self.ruta = ruta 
        self.carpetas_nominas = dict()  
        
        self.rutas_tim       = list()       
        self.nom_archivo_tim = list()
        self.periodo_tim     = list()     
        self.nom_carpeta_tim = list()
        
        self.rutas_reci         = list()
        self.nom_archivo_reci   = list()
        self.periodo_reci       = list() 
        self.nom_carpeta_reci   = list()    


        for ruta, carpetas, documentos in os.walk(self.ruta):                    
            

            for archivo in documentos:     
                
                extencion_archivo = os.path.splitext(archivo)

                if  extencion_archivo[-1] == '.pdf':
                    tipo_nomina = ruta.split('\\')[2]
                    periodo     = ruta.split('\\')[1]
                    nom_periodo = periodo + "-" + tipo_nomina
                    ruta_nom    = ruta.split('\\')[0] + "\\" + periodo + "\\" + tipo_nomina         #ruta de carpeta de cada nomina                    
                    
                   
                    ruta_completa = ruta.replace('/','\\')+ "\\" + archivo                          #ruta de archivo
                    
                    self.carpetas_nominas[nom_periodo] = ruta_nom.replace('/','\\')
                    
                    self.rutas_reci.append(ruta_completa)                   
                    self.nom_archivo_reci.append(archivo)
                    self.periodo_reci.append(periodo)
                    self.nom_carpeta_reci.append(tipo_nomina)

                elif extencion_archivo[-1] == '.xml':
                    tipo_nomina = ruta.split('\\')[2]
                    periodo     = ruta.split('\\')[1]
                    nom_periodo = periodo + "-" + tipo_nomina
                    ruta_nom    = ruta.split('\\')[0] + "\\" + periodo + "\\" + tipo_nomina         #ruta de carpeta de cada nomina

                    ruta_completa = ruta.replace('/','\\')+ "\\" + archivo                          #ruta de archivo
                    
                    self.carpetas_nominas[nom_periodo] = ruta_nom.replace('/','\\')
                                                      
                    self.rutas_tim.append(ruta_completa)
                    self.nom_archivo_tim.append(archivo)
                    self.periodo_tim.append(periodo)
                    self.nom_carpeta_tim.append(tipo_nomina)    

      
    
    






   




                
               

                        




        


