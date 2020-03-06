# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_recibos.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 383)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_start = QtWidgets.QPushButton(self.centralwidget)
        self.boton_start.setGeometry(QtCore.QRect(270, 220, 151, 41))
        self.boton_start.setStyleSheet("background-color: rgb(239, 255, 252);\n"
"")
        self.boton_start.setObjectName("boton_start")
        self.opciones = QtWidgets.QGroupBox(self.centralwidget)
        self.opciones.setGeometry(QtCore.QRect(10, 180, 151, 181))
        self.opciones.setObjectName("opciones")
        self.recuperar_rutas = QtWidgets.QCheckBox(self.opciones)
        self.recuperar_rutas.setEnabled(True)
        self.recuperar_rutas.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.recuperar_rutas.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.recuperar_rutas.setAutoFillBackground(False)
        self.recuperar_rutas.setCheckable(True)
        self.recuperar_rutas.setChecked(False)
        self.recuperar_rutas.setTristate(False)
        self.recuperar_rutas.setObjectName("recuperar_rutas")
        self.crear_log = QtWidgets.QCheckBox(self.opciones)
        self.crear_log.setGeometry(QtCore.QRect(10, 60, 131, 17))
        self.crear_log.setObjectName("crear_log")
        self.comprimir = QtWidgets.QCheckBox(self.opciones)
        self.comprimir.setGeometry(QtCore.QRect(10, 90, 131, 17))
        self.comprimir.setObjectName("comprimir")
        self.rutas = QtWidgets.QGroupBox(self.centralwidget)
        self.rutas.setGeometry(QtCore.QRect(10, 10, 521, 141))
        self.rutas.setTitle("")
        self.rutas.setObjectName("rutas")
        self.text_origen = QtWidgets.QLabel(self.rutas)
        self.text_origen.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.text_origen.setObjectName("text_origen")
        self.ruta_origen = QtWidgets.QLineEdit(self.rutas)
        self.ruta_origen.setGeometry(QtCore.QRect(90, 10, 421, 20))
        self.ruta_origen.setObjectName("ruta_origen")
        self.text_destino = QtWidgets.QLabel(self.rutas)
        self.text_destino.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.text_destino.setObjectName("text_destino")
        self.ruta_destino = QtWidgets.QLineEdit(self.rutas)
        self.ruta_destino.setGeometry(QtCore.QRect(90, 60, 421, 20))
        self.ruta_destino.setObjectName("ruta_destino")
        self.archivo_rutas = QtWidgets.QLineEdit(self.rutas)
        self.archivo_rutas.setGeometry(QtCore.QRect(90, 100, 421, 20))
        self.archivo_rutas.setObjectName("archivo_rutas")
        self.text_archivo_rutas = QtWidgets.QLabel(self.rutas)
        self.text_archivo_rutas.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.text_archivo_rutas.setObjectName("text_archivo_rutas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Copy  Recibos - Timbres"))
        self.boton_start.setText(_translate("MainWindow", "Empezar"))
        self.opciones.setTitle(_translate("MainWindow", "OPCIONES"))
        self.recuperar_rutas.setText(_translate("MainWindow", "RECUPERAR RUTAS"))
        self.crear_log.setText(_translate("MainWindow", "CREAR LOG"))
        self.comprimir.setText(_translate("MainWindow", "COMPRIMIR"))
        self.text_origen.setText(_translate("MainWindow", "Carpeta Origen"))
        self.text_destino.setText(_translate("MainWindow", "Carpeta Destino"))
        self.text_archivo_rutas.setText(_translate("MainWindow", "Archivo Rutas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
