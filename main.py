from tkinter.filedialog import asksaveasfile, askdirectory, askopenfile, askopenfilename

from recuperar_rutas.log_archivos_orig import Log_Archivos_Orig
#from copiado.copiado_archivos import copiar_archivos
#from log_y_comprimir.copiado_comprimir import ArchivoCopiado
from ui import  *
from PyQt5.QtWidgets import QDialog, QMessageBox





def ejecutar_copiado_de_archivos(ruta):
    copiar_archivos(ruta)


#crear log por nomina y comprimir
   
def crear_log(ruta):
    
    log = ArchivoCopiado(ruta)
    log.escribir_info_log()
    log.comprimir()



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
    

    def opciones_ceck(self):
        """Ejecuta el modulo segun sea la opcion elegida"""

        ruta = self.ruta_origen.text()
    
        if self.recuperar_rutas.isChecked():
            self.opcion_recuperar_rutas_enabled(True)            

            if ruta == '':
                self.mostrar_advertencia("Debe indicar una ruta")
            else:
                self.recuperar_rutas_orig(ruta)
        else:
            self.mostrar_advertencia("Seleccione una opcion")
    

    def recuperar_rutas_orig(self, ruta):
        """Llama el modulo de recuperar rutas de 
            recibos y timbres de nominas"""

        log = Log_Archivos_Orig(ruta)
        log.ejecutar(asksaveasfile())

        self.opcion_recuperar_rutas_enabled(False)

    
    def opcion_recuperar_rutas_enabled(self, valor):
        """Opciones habilitadas o desabilitadas segun sea el caso
         True o False"""

        self.opciones.setDisabled(valor)
        self.ruta_destino.setDisabled(valor)
        self.archivo_rutas.setDisabled(valor)

        


   
    def mostrar_advertencia(self, texto):
        """Muestra advertencias"""

        QMessageBox.warning(self, "Advertencia", texto)   




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

