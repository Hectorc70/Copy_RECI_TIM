# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_p1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana(object):
    def setupUi(self, ventana):
        ventana.setObjectName("ventana")
        ventana.setEnabled(True)
        ventana.resize(285, 218)
        ventana.setWindowOpacity(0.0)
        ventana.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(ventana)
        self.centralwidget.setObjectName("centralwidget")
        self.b1_rutas_orig = QtWidgets.QPushButton(self.centralwidget)
        self.b1_rutas_orig.setGeometry(QtCore.QRect(10, 10, 101, 51))
        self.b1_rutas_orig.setObjectName("b1_rutas_orig")
        self.b2_copiar_archivos = QtWidgets.QPushButton(self.centralwidget)
        self.b2_copiar_archivos.setGeometry(QtCore.QRect(170, 10, 101, 51))
        self.b2_copiar_archivos.setObjectName("b2_copiar_archivos")
        ventana.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ventana)
        self.statusbar.setObjectName("statusbar")
        ventana.setStatusBar(self.statusbar)

        self.retranslateUi(ventana)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def retranslateUi(self, ventana):
        _translate = QtCore.QCoreApplication.translate
        ventana.setWindowTitle(_translate("ventana", "MainWindow"))
        self.b1_rutas_orig.setText(_translate("ventana", "OBTENER RUTAS"))
        self.b2_copiar_archivos.setText(_translate("ventana", "COPIAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = QtWidgets.QMainWindow()
    ui = Ui_ventana()
    ui.setupUi(ventana)
    ventana.show()
    sys.exit(app.exec_())
