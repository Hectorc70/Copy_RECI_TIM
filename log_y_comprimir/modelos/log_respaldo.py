

from log_y_comprimir.modelos.log import Log
from log_y_comprimir.modelos.rutas import Rutas

class Log_Destino(Log, Rutas):
    """Crea log por nomina llamando a la clase
       Log"""
    

    def __init__(self, carpeta_lec):
        self.carpeta_lect = carpeta_lec
            
        Rutas.__init__(self)
        self.recuperar_rutas_archivos(self.carpeta_lect)
      
        self.hoja1_titulo = "Archivos PDF"
        Log.__init__(self, self.hoja1_titulo)


    
    def escribir_rutas_pdf(self):
        """llama la clase Log que lee y escribe rutas de los
            recibos de Nomina o Listados"""

    

        hoja_activa = 0
        columna_inicial = 1
        fila = 1

        
        titulos = ["Archivo", "Nomina","Periodo","Ruta de Archivo"]
        lista   = [self.nom_archivo_reci, self.nom_carpeta_reci,
                    self.periodo_reci, self.rutas_reci
        ]

        

        self.escribir_titulo(titulos, fila, hoja_activa)
        self.escribir_en_hoja(lista, columna_inicial, hoja_activa)
       

        
            

    def escribir_rutas_xml(self):
        """llama la clase log que lee y escribe rutas de los
           timbres de las Nominas"""  

        
        
        columna_inicial = 1
        fila = 1

        self.crear_hoja_nueva("Timbres_XML")
        hoja_activa = 1
        
        titulos  = ["Archivo", "Nomina","Periodo","Ruta de Archivo"]
        lista   = [self.nom_archivo_tim, self.nom_carpeta_tim,
                    self.periodo_tim,
                    self.rutas_tim
        ]


        self.escribir_titulo(titulos, fila, hoja_activa)
        self.escribir_en_hoja(lista, columna_inicial, hoja_activa)
       
        
    def guardar(self, ruta):
                
        self.ruta_guardar = ruta
        self.guardar_archivo_log(self.ruta_guardar)
   





    



    