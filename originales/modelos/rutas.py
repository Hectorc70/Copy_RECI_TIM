import os
import os.path



class Rutas():

    def __init__(self, ruta):
        self.ruta_obtener_carpeta = ruta
        self.recuperar_rutas()
        self.depurar_archivos_pdf()
        self.depurar_archivos_xml()

    def recuperar_rutas(self):
        """Recupera las Rutas de Archivos PDF y XML"""
       
        
        self.rutas_pdf = list()
        self.rutas_xml = list()
       
        

        for ruta, carpetas, documentos in os.walk(self.ruta_obtener_carpeta,topdown = True):                      
          
            
            for archivo in documentos:
            

                extencion_archivo = os.path.splitext(archivo)

                if  extencion_archivo[-1] == '.pdf':

                    ruta_completa = ruta.replace('/','\\')+ "\\" + archivo
                    self.rutas_pdf.append(ruta_completa)

                    

                elif extencion_archivo[-1] == '.xml' and extencion_archivo[0] != 'metadata':

                    ruta_completa = ruta.replace('/','\\') + "\\" + archivo
                    self.rutas_xml.append(ruta_completa)
        print("Archivos de Carpeta Obtenidos")

                    

    
    
    
    
    def depurar_archivos_pdf(self):
        """solo deja los archivos pdf
            que se requieren en el log"""



        self.recibos_pdf         = list()
        self.periodo             = list()
        self.recibos_pdf_destino = list()

        PERIODOS = ['01','02','03','04','05','06','07','08','09','10','11',
                    '12','13','14','15','16','17','18','19','20','21','22','23','24']

        
        for ruta_pdf in self.rutas_pdf:
            
            ruta_split = ruta_pdf.split('\\')             

            año_periodo = ruta_pdf.split('\\')[2]
            periodo     = año_periodo.split('_')[0]

            archivo     = ruta_pdf.split('\\')[-1]
            hoja_control= archivo.split('_')[0] 
            nomina      = ruta_pdf.split('\\')[3]
            


            ruta_split.pop(0)
            ruta_destino = "Y:"+"\\" + "\\".join(ruta_split)


                        
            if (nomina == 'JUBILADOS_PDF' and hoja_control != 'Control' and 
                periodo in PERIODOS):

                subcarpeta  = ruta_pdf.split('\\')[4]

                if subcarpeta != 'LISTADOS':    
                    print("------Obteniendo Recibos PDF------")            
                    self.recibos_pdf.append(ruta_pdf)
                    self.periodo.append(año_periodo)
                    self.recibos_pdf_destino.append(ruta_destino)

            elif (nomina != 'JUBILADOS_PDF' and nomina != 'ORDENES_JUDICIALES' and
                  periodo in PERIODOS and hoja_control != 'Control'):              
                 
                try:
                    subcarpeta  = ruta_pdf.split('\\')[5]
                except IndexError:
                    print(ruta_pdf)
                    break
                

                if subcarpeta != 'LISTADOS':  
                    #print("------Obteniendo Recibos PDF------")              
                    self.recibos_pdf.append(ruta_pdf)
                    self.periodo.append(año_periodo)
                    self.recibos_pdf_destino.append(ruta_destino)

        print("------RECIBOS OBTENIDOS------")
        
         
                
    def depurar_archivos_xml(self):
        """Escluye los archivos que no son timbres de
            todas las nóminas"""

       

        self.timbres              = list()
        self.periodo_timbres              =  list()
        self.ruta_destino_timbres = list()

        PERIODOS           = ['01','02','03','04','05','06','07','08','09','10','11',
                              '12','13','14','15','16','17','18','19','20','21','22','23','24']
        CARPETAS_EXCLUIDAS = ['_SYNCAPP']


        for ruta_xml in self.rutas_xml:
            ruta_split = ruta_xml.split('\\')
            año_periodo = ruta_xml.split('\\')[2]
            periodo     = año_periodo.split('_')[0]
            carpeta     = ruta_xml.split('\\')[3]         
            
            ruta_split.pop(0)
            ruta_destino = "Y:"+"\\" + "\\".join(ruta_split)
            

            if carpeta not in CARPETAS_EXCLUIDAS and periodo in PERIODOS:

                self.timbres.append(ruta_xml)
                self.periodo_timbres.append(año_periodo)
                self.ruta_destino_timbres.append(ruta_destino)

                #print("------Obteniendo Timbres XML------")
        print("------TIMBRES OBTENIDOS------")


            
    



   




                
               

                        




        


