# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1093, 797)
        self.accionGuardar = QAction(MainWindow)
        self.accionGuardar.setObjectName(u"accionGuardar")
        self.accionAbrir = QAction(MainWindow)
        self.accionAbrir.setObjectName(u"accionAbrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.blue = QSpinBox(self.groupBox)
        self.blue.setObjectName(u"blue")
        self.blue.setMaximum(255)

        self.gridLayout.addWidget(self.blue, 7, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.ox = QSpinBox(self.groupBox)
        self.ox.setObjectName(u"ox")
        self.ox.setMaximum(500)

        self.gridLayout.addWidget(self.ox, 0, 1, 1, 1)

        self.velocidad = QSpinBox(self.groupBox)
        self.velocidad.setObjectName(u"velocidad")
        self.velocidad.setMaximum(999)

        self.gridLayout.addWidget(self.velocidad, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.green = QSpinBox(self.groupBox)
        self.green.setObjectName(u"green")
        self.green.setMaximum(255)

        self.gridLayout.addWidget(self.green, 6, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.dy = QSpinBox(self.groupBox)
        self.dy.setObjectName(u"dy")
        self.dy.setMaximum(500)

        self.gridLayout.addWidget(self.dy, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.dx = QSpinBox(self.groupBox)
        self.dx.setObjectName(u"dx")
        self.dx.setMaximum(500)

        self.gridLayout.addWidget(self.dx, 2, 1, 1, 1)

        self.insertar_final = QPushButton(self.groupBox)
        self.insertar_final.setObjectName(u"insertar_final")

        self.gridLayout.addWidget(self.insertar_final, 8, 1, 1, 1)

        self.oy = QSpinBox(self.groupBox)
        self.oy.setObjectName(u"oy")
        self.oy.setMaximum(500)

        self.gridLayout.addWidget(self.oy, 1, 1, 1, 1)

        self.red = QSpinBox(self.groupBox)
        self.red.setObjectName(u"red")
        self.red.setMaximum(255)

        self.gridLayout.addWidget(self.red, 5, 1, 1, 1)

        self.insertar_inicio = QPushButton(self.groupBox)
        self.insertar_inicio.setObjectName(u"insertar_inicio")

        self.gridLayout.addWidget(self.insertar_inicio, 8, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.lista_particulas = QPlainTextEdit(self.tab)
        self.lista_particulas.setObjectName(u"lista_particulas")

        self.gridLayout_2.addWidget(self.lista_particulas, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buscar_lineedit = QLineEdit(self.tab_2)
        self.buscar_lineedit.setObjectName(u"buscar_lineedit")

        self.gridLayout_3.addWidget(self.buscar_lineedit, 1, 0, 1, 1)

        self.Buscar_pushbutton = QPushButton(self.tab_2)
        self.Buscar_pushbutton.setObjectName(u"Buscar_pushbutton")

        self.gridLayout_3.addWidget(self.Buscar_pushbutton, 2, 0, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 10, 1051, 701))
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1093, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.accionAbrir)
        self.menuArchivo.addAction(self.accionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.accionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.accionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.accionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.accionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RED ( 0-255 )", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y  ( 0-500 )", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Origen Y ( 0-500 )", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"BLUE ( 0-255 )", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"GREEN ( 0-255 )", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X  ( 0-500 )", None))
        self.insertar_final.setText(QCoreApplication.translate("MainWindow", u"Insertar al Final", None))
        self.insertar_inicio.setText(QCoreApplication.translate("MainWindow", u"Insertar al Inicio", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen X ( 0-500 )", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad ( KM/h )", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar Particulas", None))
        self.buscar_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escribe un ID", None))
        self.Buscar_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla de Particulas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Particulas", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

