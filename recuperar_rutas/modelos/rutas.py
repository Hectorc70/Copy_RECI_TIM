import os



class Rutas():
    """Recupera rutas de una carpeta dada"""
    
    def __init__(self, carpeta_a_leer):

        self.carpeta = carpeta_a_leer
        


    def recuperar_rutas(self):         
        rutas = list()        
       

        for ruta, carpetas, archivos in os.walk(self.carpeta,topdown = True):          
            
            for archivo in archivos:
                    
                ruta_full = self.ruta_completa(ruta, archivo)                
                rutas.append(ruta_full)
        
        
        return rutas
        

    def recuperar_carpetas(self):

        carpetas_recuperadas = list()

        for ruta, carpetas, archivos in os.walk(self.carpeta,topdown = True):          
            
            for carpeta in carpetas:
                    
                ruta_full = self.ruta_completa(ruta, carpeta)                
                carpetas_recuperadas.append(ruta_full)
        
        
        return carpetas_recuperadas

                    
     
    
    def ruta_completa(self, ruta, archivo ):
        """Devuelve la ruta completa. Ejemplo: entrada(ruta='C:/documents', archivo='ejemplo.txt'),
        salida(ruta_completa='C:\\documents\\ejemplo.txt')"""

          
        ruta_completa = ruta.replace('/','\\')+ "\\" + archivo
            
        return ruta_completa

    
    def unir_cadenas(self, separador, lista_datos):

        cadena = separador.join(lista_datos)

        return cadena

    
    
   
    