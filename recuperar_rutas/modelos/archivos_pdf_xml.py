import os
from os.path import splitext
from tkinter.filedialog import askdirectory

from recuperar_rutas.modelos.rutas import Rutas, unir_cadenas

PERIODOS = ['01','02','03','04','05','06','07','08','09','10','11',
			'12','13','14','15','16','17','18','19','20','21','22','23','24'
			]
	

class ArchivosOrig():     
	
	def __init__(self, ruta_Carpeta):

		self.ruta_base = ruta_Carpeta

		self.rutas = Rutas(self.ruta_base)
		self.rutas_archivos = self.rutas.recuperar_rutas()

		

	def depurar_rutas(self):
		
		self.rutas_pdf 	  = list()
		self.rutas_xml = list()
		
		for ruta_archivo in self.rutas_archivos:

			extencion_archivo = splitext(ruta_archivo)
			
			if extencion_archivo[-1] == '.pdf':
				rutas_pdf = self.archivos_pdf(ruta_archivo)
				if rutas_pdf == None:
					continue
				else:
					self.rutas_pdf.append(rutas_pdf)			

			elif extencion_archivo[-1] == '.xml' or extencion_archivo[-1] == 'XML':
				rutas_xml = self.archivos_xml(ruta_archivo)
				if rutas_xml == None:
					continue
				else:
					self.rutas_xml.append(rutas_xml)
		
		return [self.rutas_pdf, self.rutas_xml]
		



	def archivos_pdf(self, ruta_pdf):
		"""solo deja los archivos pdf""" 

		recibos_pdf   = list()
		periodo       = list()
		nombre_nomina = list()   
		recibos_pdf_ruta = list()	
		recibos_ruta_sb = list()

		datos_ruta = self.datos_ruta(ruta_pdf) 
		#hoja_control = datos_ruta['RUTA-DIV'][-1].split('_')
		hoja_control  = datos_ruta['SUBCARPETA'].split('_')[0]


		if (datos_ruta['PERIODO'] in PERIODOS and 
			datos_ruta['NOMINA'] == 'JUBILADOS_PDF'
			):
			if (hoja_control != 'Control' and
				datos_ruta['SUBCARPETA'] == 'RECIBOS'):
			
				recibos_pdf.append(datos_ruta['ARCHIVO'])
				recibos_pdf_ruta.append(datos_ruta['RUTA'])
				recibos_ruta_sb.append(datos_ruta['RUTA-SB'])
				periodo.append(datos_ruta['AÑO-PERIODO'])
				nombre_nomina.append(datos_ruta['NOMINA'])
				

				return (periodo, nombre_nomina, 
						recibos_pdf, recibos_pdf_ruta, 
						recibos_ruta_sb
				)


		elif (datos_ruta['PERIODO'] in PERIODOS and 
			  datos_ruta['NOMINA'] != 'JUBILADOS_PDF'):

			if (hoja_control != 'Control' and
				datos_ruta['SUBCARPETA-2'] != 'LISTADOS'):

					recibos_pdf.append(datos_ruta['ARCHIVO'])
					recibos_pdf_ruta.append(datos_ruta['RUTA'])
					recibos_ruta_sb.append(datos_ruta['RUTA-SB'])
					periodo.append(datos_ruta['AÑO-PERIODO'])
					nombre_nomina.append(datos_ruta['NOMINA'])

					return (periodo, nombre_nomina, 
							recibos_pdf, recibos_pdf_ruta, 
							recibos_ruta_sb
					)
		
		
	def archivos_xml(self, ruta_xml):
		"""Escluye los archivos que no son timbres de
			todas las nóminas"""

	   

		timbres         = list()
		timbres_ruta    = list()
		periodo_timbres =  list()
		nombre_nomina   = list()   
		timbres_ruta_sb = list()
		
		CARPETAS_EXCLUIDAS = ['_SYNCAPP',' ']					

		datos_ruta = self.datos_ruta(ruta_xml)
		if (datos_ruta['PERIODO'] in PERIODOS and 
			datos_ruta['NOMINA'] not in CARPETAS_EXCLUIDAS):
			
			timbres.append(datos_ruta['ARCHIVO'])
			timbres_ruta.append(datos_ruta['RUTA'])
			timbres_ruta_sb.append(datos_ruta['RUTA-SB'])
			periodo_timbres.append(datos_ruta['AÑO-PERIODO'])
			nombre_nomina.append(datos_ruta['NOMINA'])
		
			return (periodo_timbres, nombre_nomina, 
					timbres, timbres_ruta, 
					timbres_ruta_sb
			)
		
				
			
	def datos_ruta(self, ruta_archivo):
		"""Devuelve datos de una ruta de archivo pdf o xml"""
		
		ruta_base_contador  = len(self.ruta_base.split("\\"))		
		ruta_split 			= ruta_archivo.split('\\')
		archivo    			= ruta_split[-1] 		
		ruta_sin_base 		= self.separar_ruta(ruta_archivo)

		año_periodo = ruta_split[ruta_base_contador]
		periodo     = año_periodo.split("_")[0]

		try:	
			datos = {'AÑO-PERIODO': año_periodo, 'PERIODO':periodo, 
					 'NOMINA':ruta_split[ruta_base_contador+1], 'ARCHIVO':archivo,
					 'SUBCARPETA':ruta_split[ruta_base_contador+2], 'SUBCARPETA-2':ruta_split[ruta_base_contador+3],
					 'RUTA':ruta_archivo, 'RUTA-SB':ruta_sin_base
					}
			return datos

		except IndexError:

			datos = {'AÑO-PERIODO': None, 'PERIODO':None, 
					 'NOMINA':' ', 'ARCHIVO':'',
					'SUBCARPETA':'', 'SUBCARPETA-2':'','RUTA':ruta_archivo
					}
			return datos
	
	def separar_ruta(self, ruta):
		ruta_base_split = self.ruta_base.split('\\')
		ruta = ruta.split('\\')
		

		for elemento_ruta in ruta_base_split:
			ruta.remove(elemento_ruta)

		ruta_sin_base = unir_cadenas('\\', ruta)	
		
		return ruta_sin_base


		

		 
				


	



#arc = ArchivosOrig(askdirectory())
#arc.depurar_rutas()

			
	



   




				
			   

						




		


