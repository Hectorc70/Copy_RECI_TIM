from tkinter.filedialog import asksaveasfile, askdirectory, askopenfile, askopenfilename

from PyQt5.QtWidgets import QDialog, QMessageBox

from recuperar_rutas.log_archivos_orig import Log_Archivos_Orig
from copiado.copiado_archivos import CopiadoArchivos
#from log_y_comprimir.copiado_comprimir import ArchivoCopiado
from ui import  *







#crear log por nomina y comprimir
   
#def crear_log(ruta):
	
#	log = ArchivoCopiado(ruta)
#	log.escribir_info_log()
#	log.comprimir()



#recuperar_rutas_orig()
#ejecutar_copiado_de_archivos(askopenfile())
#crear_log(askdirectory())

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

		log = Log_Archivos_Orig(ruta)
		log.ejecutar(asksaveasfile(mode='w', defaultextension=".xlsx"))

		self.opcion_recuperar_rutas_enabled(False)

	
	def ejecutar_copiado_de_archivos(self, ruta_destino):
		
		
		archivos = CopiadoArchivos(askopenfile())
		archivos.ejecutar(ruta_destino)

		self.opcion_copiar_enabled(False)
	

	def opciones_ceck(self):
		"""Ejecuta el modulo segun sea la opcion elegida"""

		ruta = self.ruta_origen.text()
		ruta_destino = self.ruta_destino.text()
	
		if self.recuperar_rutas.isChecked():
			self.opcion_recuperar_rutas_enabled(True)            

			if ruta == '':
				self.mostrar_advertencia("Debe indicar una ruta")
			else:
				self.recuperar_rutas_orig(ruta)
		
		if self.copiar.isChecked():
			self.opcion_copiar_enabled(True)
			if ruta_destino == '':
				self.mostrar_advertencia("Indique una ruta C:\\CARPETA")
			else:
				self.ejecutar_copiado_de_archivos(ruta_destino)

		
		else:
			self.mostrar_advertencia("Seleccione una opcion")
	
	def opcion_recuperar_rutas_enabled(self, valor):
		"""Opciones habilitadas o desabilitadas segun sea el caso
		 True o False"""

		self.opciones.setDisabled(valor)
		self.ruta_destino.setDisabled(valor)
		

	def opcion_copiar_enabled(self, valor):
		self.opciones.setDisabled(valor)
		self.ruta_origen.setDisabled(valor)
		

   
	def mostrar_advertencia(self, texto):
		"""Muestra advertencias"""

		QMessageBox.warning(self, "Advertencia", texto)   


   


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()

