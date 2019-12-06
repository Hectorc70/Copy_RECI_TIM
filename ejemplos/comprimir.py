import zipfile




class ArchivoComprimido:

    def comprimir(self):

        archivo = 'C:\Proyects_Ayto\Recibos_Timbres_Copiar\ejemplos\pur.pdf'
        ruta_g  = 'C:\RECIBOS_PDF_NOMINA_2019\comprimido_pru.zip' 
            
        comprimir = zipfile.ZipFile(ruta_g, 'w')
        comprimir.write(archivo, compress_type=zipfile.ZIP_DEFLATED)
 
        comprimir.close()
        print("Archivo comprimido")  


c = ArchivoComprimido()
c.comprimir()