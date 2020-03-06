import os
from os.path import splitext
from tkinter.filedialog import askdirectory

from recuperar_rutas.modelos.rutas import Rutas

PERIODOS = ['01','02','03','04','05','06','07','08','09','10','11',
			'12','13','14','15','16','17','18','19','20','21','22','23','24'
			]
	

class ArchivosOrig():     
	
	def __init__(self, ruta_Carpeta):

		self.ruta_base = ruta_Carpeta

		rutas = Rutas(self.ruta_base)
		self.rutas_archivos = rutas.recuperar_rutas()

		

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

		self.recibos_pdf   = list()
		self.periodo       = list()
		self.nombre_nomina = list()   
		self.recibos_pdf_ruta = list()	

		datos_ruta = self.datos_ruta(ruta_pdf) 
		#hoja_control = datos_ruta['RUTA-DIV'][-1].split('_')
		hoja_control  = datos_ruta['SUBCARPETA'].split('_')[0]


		if (datos_ruta['PERIODO'] in PERIODOS and 
			datos_ruta['NOMINA'] == 'JUBILADOS_PDF'
			):
			if (hoja_control != 'Control' and
				datos_ruta['SUBCARPETA'] == 'RECIBOS'):
			
				self.recibos_pdf.append(datos_ruta['ARCHIVO'])
				self.recibos_pdf_ruta.append(datos_ruta['RUTA'])
				self.periodo.append(datos_ruta['AÑO-PERIODO'])
				self.nombre_nomina.append(datos_ruta['NOMINA'])			

				return self.periodo, self.nombre_nomina, self.recibos_pdf, self.recibos_pdf_ruta


		elif (datos_ruta['PERIODO'] in PERIODOS and 
			  datos_ruta['NOMINA'] != 'JUBILADOS_PDF'):

			if (hoja_control != 'Control' and
				datos_ruta['SUBCARPETA-2'] != 'LISTADOS'):

					self.recibos_pdf.append(datos_ruta['ARCHIVO'])
					self.recibos_pdf_ruta.append(datos_ruta['RUTA'])
					self.periodo.append(datos_ruta['AÑO-PERIODO'])
					self.nombre_nomina.append(datos_ruta['NOMINA'])

					return self.periodo, self.nombre_nomina, self.recibos_pdf, self.recibos_pdf_ruta
		
		

		
				
			
	def datos_ruta(self, ruta_archivo):
		"""Devuelve datos de una ruta de archivo pdf o xml"""
		
		ruta_base  = len(self.ruta_base.split("\\"))		
		ruta_split = ruta_archivo.split('\\')
		archivo    = ruta_split[-1] 
		#ruta_split.pop(-1)

		#ruta_sin_archivo = '\\'.join(ruta_split)

		año_periodo = ruta_split[ruta_base]
		periodo     = año_periodo.split("_")[0]

		try:	
			datos = {'AÑO-PERIODO': año_periodo, 'PERIODO':periodo, 
					 'NOMINA':ruta_split[ruta_base+1], 'ARCHIVO':archivo,
					 'SUBCARPETA':ruta_split[ruta_base+2], 'SUBCARPETA-2':ruta_split[ruta_base+3],
					 'RUTA':ruta_archivo
					}
			return datos

		except IndexError:

			datos = {'AÑO-PERIODO': None, 'PERIODO':None, 
					 'NOMINA':' ', 'ARCHIVO':'',
					'SUBCARPETA':'', 'SUBCARPETA-2':'','RUTA':ruta_archivo
					}
			return datos
	
		 
				
	def archivos_xml(self, ruta_xml):
		"""Escluye los archivos que no son timbres de
			todas las nóminas"""

	   

		self.timbres         = list()
		self.timbres_ruta         = list()
		self.periodo_timbres =  list()
		self.nombre_nomina   = list()   
		
		CARPETAS_EXCLUIDAS = ['_SYNCAPP',' ']					

		datos_ruta = self.datos_ruta(ruta_xml)
		if datos_ruta['PERIODO'] in PERIODOS and datos_ruta['NOMINA'] not in CARPETAS_EXCLUIDAS:
			self.timbres.append(datos_ruta['ARCHIVO'])
			self.timbres_ruta.append(datos_ruta['RUTA'])
			self.periodo_timbres.append(datos_ruta['AÑO-PERIODO'])
			self.nombre_nomina.append(datos_ruta['NOMINA'])
		
			return self.periodo_timbres, self.nombre_nomina, self.timbres, self.timbres_ruta

	



#arc = ArchivosOrig(askdirectory())
#arc.depurar_rutas()

			
	



   




				
			   

						




		


