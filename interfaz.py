

from tkinter.filedialog import asksaveasfile, askdirectory, askopenfile



from ui import *
from main import *




class MainWindow(QtWidgets.QMainWindow, Ui_ventana):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi()
        

        #self.b1_rutas_orig.clicked.connect(self.Buscar_en_carpeta)
        #self.b2_copiar_archivos.clicked.connect(self.copiar_archivos)

        pass
    
    def Buscar_en_carpeta(self, ruta):
        recuperar_rutas_orig()

    def copiar_archivos(self):
        ejecutar_copiado_de_archivos(askopenfile())


   
        




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_() 