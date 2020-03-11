from tkinter.filedialog import asksaveasfile, askdirectory, askopenfile, askopenfilename

from PyQt5.QtWidgets import QDialog, QMessageBox

from recuperar_rutas.log_archivos_orig import Log_Archivos_Orig
from copiado_comprimir.copiado_archivos import CopiadoArchivos
from copiado_comprimir.comprimir import ComprimirArchivo
from ui import  *





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		
		self.setupUi(self)
		
		self.ejecutar()


	



	def ejecutar(self):    

		self.boton_start.clicked.connect(self.opciones_ceck)

	def recuperar_rutas_orig(self, ruta):
		"""Llama el modulo de recuperar rutas de 
			recibos y timbres de nominas"""
		self.estado_opciones_iniciales(True)
		log = Log_Archivos_Orig(ruta)
		log.ejecutar(asksaveasfile(mode='w', defaultextension=".xlsx"))
		self.estado_opciones_iniciales(False)

		

	
	def ejecutar_copiado_de_archivos(self, ruta_destino):
		self.estado_opciones_iniciales(True)
		
		archivos = CopiadoArchivos(askopenfile())
		archivos.ejecutar(ruta_destino)
		self.estado_opciones_iniciales(False)
		
	
	def comprimir_archivos(self, ruta):
		self.estado_opciones_iniciales(True)
		archivos_comprimidos = ComprimirArchivo(ruta)
		archivos_comprimidos.ejecutar_compresor()
		self.estado_opciones_iniciales(False)
	

	def opciones_ceck(self):
		"""Ejecuta el modulo segun sea la opcion elegida"""

		ruta = self.ruta_origen.text()
		ruta_destino = self.ruta_destino.text()
	
		if self.recuperar_rutas.isChecked():			     

			if ruta == '':
				self.mostrar_advertencia("Debe indicar una ruta")
			else:
				self.recuperar_rutas_orig(ruta)
		
		if self.copiar.isChecked():
			
			if ruta_destino == '':
				self.mostrar_advertencia("Indique una ruta C:\\CARPETA")
			else:
				self.ejecutar_copiado_de_archivos(ruta_destino)

		if self.comprimir.isChecked():
			self.ruta_destino.setDisabled(True)
			if ruta == '':
				self.mostrar_advertencia("Debe llenar el campo de Carpeta Origen")
			else:
				self.comprimir_archivos(ruta)



		
		else:
			self.mostrar_advertencia("Seleccione una opcion")
	
		
	def estado_opciones_iniciales(self, valor):
		self.ruta_destino.setDisabled(valor)
		self.ruta_origen.setDisabled(valor)
		self.opciones.setDisabled(valor)
		
   
	def mostrar_advertencia(self, texto):
		"""Muestra advertencias"""

		QMessageBox.warning(self, "Advertencia", texto)   


   


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()

