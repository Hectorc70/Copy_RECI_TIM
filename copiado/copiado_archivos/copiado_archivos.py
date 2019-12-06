

from copiado.copiado_archivos.modelos.archivos import Archivo





class Archivo_pdf(Archivo):

    def __init__(self, documento):
        Archivo.__init__(self, documento)
        self.hoja = 'Archivos PDF' 

        self.ejecutar_pdf() 


        



    def ejecutar_pdf(self):
        self.copiar_archivos(self.hoja)
        print("ARCHIVOS COPIADOS")
       







class Archivo_xml(Archivo):
    
    def __init__(self, documento):
        Archivo.__init__(self, documento)
        self.hoja = 'Timbres_XML'

        self.ejecutar_xml()
    
         
    def ejecutar_xml(self):
        self.copiar_archivos(self.hoja)
        print("ARCHIVOS COPIADOS")


        



   

        
def copiar_archivos(doc):    

        Archivo_pdf(doc)
        Archivo_xml(doc)





       

