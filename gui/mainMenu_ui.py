# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 782, 582))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayoutWidget_2 = QWidget(self.page)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 780, 581))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.seedSpin = QSpinBox(self.verticalLayoutWidget_2)
        self.seedSpin.setObjectName(u"seedSpin")

        self.horizontalLayout_6.addWidget(self.seedSpin)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.algCombo = QComboBox(self.verticalLayoutWidget_2)
        self.algCombo.setObjectName(u"algCombo")

        self.horizontalLayout_8.addWidget(self.algCombo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.fileEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.fileEdit.setObjectName(u"fileEdit")

        self.horizontalLayout_9.addWidget(self.fileEdit)

        self.browseBtn = QPushButton(self.verticalLayoutWidget_2)
        self.browseBtn.setObjectName(u"browseBtn")

        self.horizontalLayout_9.addWidget(self.browseBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.processCombo = QComboBox(self.verticalLayoutWidget_2)
        self.processCombo.setObjectName(u"processCombo")

        self.horizontalLayout_10.addWidget(self.processCombo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.operationCombo = QComboBox(self.verticalLayoutWidget_2)
        self.operationCombo.setObjectName(u"operationCombo")

        self.horizontalLayout_11.addWidget(self.operationCombo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.exitBtn = QPushButton(self.verticalLayoutWidget_2)
        self.exitBtn.setObjectName(u"exitBtn")

        self.horizontalLayout_12.addWidget(self.exitBtn)

        self.startBtn = QPushButton(self.verticalLayoutWidget_2)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_12.addWidget(self.startBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Algoritmos de paginaci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Semilla para random:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Algoritmo a simular:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Archivo para simular:", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Navegar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de procesos a simular:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Cantidad de operaciones:", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Iniciar Simulaci\u00f3n", None))
    # retranslateUi

