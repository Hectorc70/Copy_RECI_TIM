import os
import os.path as path 
from os import makedirs
import zipfile
from tkinter.filedialog import askdirectory, askopenfile

from copiado_archivos import CopiadoArchivos
from modelos.rutas import Rutas
from modelos.rutas import unir_cadenas, dividir_cadena

PERIODOS = ['01','02','03','04','05','06','07','08','09','10','11',
			'12','13','14','15','16','17','18','19','20','21','22','23','24'
			]

class ComprimirArchivo():
	
	def __init__(self, archivo, ruta_destino):
		#archivos = CopiadoArchivos(archivo)
		#archivos.ejecutar(ruta_destino)

		self.carpeta_lectura = ruta_destino
		self.rutas = Rutas(self.carpeta_lectura)

	def creacion_carpeta(self):

		        
		ruta_carpetas =self.rutas.recuperar_carpetas(True)
		
		

		ruta_archivos_compri = self.carpeta_lectura + '\\' + 'COMPRIMIDOS'
		
		if path.exists( ruta_archivos_compri):
			self.comprimir(ruta_carpetas, ruta_archivos_compri)
				
				
		else:
			makedirs(ruta_archivos_compri, exist_ok=True)
			self.comprimir(ruta_carpetas, ruta_archivos_compri)

	def comprobar_periodos_comprimidos(self, ruta_carpeta):
		carpetas_comprimidas = list()

		rutas_archivos = self.rutas.recuperar_rutas(ruta_carpeta, True)

		for ruta_archivo in rutas_archivos:
			archivo = ruta_archivo[-1]
			archivo_s_extencion = archivo.split('.')[0]

			carpetas_comprimidas.append(archivo_s_extencion)

			
		
		return carpetas_comprimidas





		


	def comprimir(self, carpetas, r_comprimir):
		
		
		carpetas_comprimidas = self.comprobar_periodos_comprimidos(r_comprimir)
		 
		for carpeta in carpetas:
			carpeta_div = dividir_cadena('\\', carpeta)
			año_periodo = carpeta_div[-1]
			periodo = año_periodo.split('_')[0]
			

			


			if periodo in PERIODOS:
				if año_periodo in carpetas_comprimidas:
					continue 
			
				
			
				archivos = self.rutas.recuperar_rutas(carpeta, True)
				ruta_comprimidos = zipfile.ZipFile(r_comprimir + '\\'+ año_periodo + ".zip", 'w')
			
				for archivo in archivos:

					archivo_ruta = unir_cadenas('\\', archivo)

					for item in carpeta_div:
						archivo.remove(item)

					nombre_archivo = unir_cadenas('\\', archivo)
					

					ruta_comprimidos.write(archivo_ruta, nombre_archivo)

				ruta_comprimidos.close()
			else:
				continue
		
			
			

				
			
			
		

c = ComprimirArchivo(askopenfile(), askdirectory())
c.creacion_carpeta()





		
   

  
class ArchivoCopiadoLog:

	def __init__(self):
		pass

	def escribir_info_log(self, carpetas_nominas):  
		"""Escribe un log por cada carpeta(Tipo de Nomina)"""  
		
	  

		for ruta_nom in carpetas_nominas.values():
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
	










	
			   
				
			
				   




	




	   

