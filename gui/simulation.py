# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulation.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.optGroupBox = QGroupBox(self.centralwidget)
        self.optGroupBox.setObjectName(u"optGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.optGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.optGroupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.optGroupBox)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMaximumSize(QSize(16777215, 250))
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_15 = QLabel(self.optGroupBox)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 7, 1, 1, 1)

        self.label_5 = QLabel(self.optGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 1, 1, 1)

        self.label_12 = QLabel(self.optGroupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 2)

        self.label_4 = QLabel(self.optGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_11 = QLabel(self.optGroupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 5, 1, 1, 1)

        self.label_14 = QLabel(self.optGroupBox)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 7, 0, 1, 1)

        self.label_7 = QLabel(self.optGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_10 = QLabel(self.optGroupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_8 = QLabel(self.optGroupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.optGroupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)

        self.label_13 = QLabel(self.optGroupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 6, 0, 1, 2)

        self.label_6 = QLabel(self.optGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_16 = QLabel(self.optGroupBox)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 8, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.horizontalLayout.addWidget(self.optGroupBox)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_44 = QLabel(self.groupBox)
        self.label_44.setObjectName(u"label_44")
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_44)

        self.tableWidget_3 = QTableWidget(self.groupBox)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy1.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy1)
        self.tableWidget_3.setMaximumSize(QSize(16777215, 250))
        self.tableWidget_3.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        self.verticalLayout_5.addWidget(self.tableWidget_3)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_45 = QLabel(self.groupBox)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_5.addWidget(self.label_45, 7, 1, 1, 1)

        self.label_46 = QLabel(self.groupBox)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_5.addWidget(self.label_46, 3, 1, 1, 1)

        self.label_47 = QLabel(self.groupBox)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_47, 4, 0, 1, 2)

        self.label_48 = QLabel(self.groupBox)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_5.addWidget(self.label_48, 3, 0, 1, 1)

        self.label_49 = QLabel(self.groupBox)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_5.addWidget(self.label_49, 5, 1, 1, 1)

        self.label_50 = QLabel(self.groupBox)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_5.addWidget(self.label_50, 7, 0, 1, 1)

        self.label_51 = QLabel(self.groupBox)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_5.addWidget(self.label_51, 1, 1, 1, 1)

        self.label_52 = QLabel(self.groupBox)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_5.addWidget(self.label_52, 5, 0, 1, 1)

        self.label_53 = QLabel(self.groupBox)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_5.addWidget(self.label_53, 2, 0, 1, 1)

        self.label_54 = QLabel(self.groupBox)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_5.addWidget(self.label_54, 2, 1, 1, 1)

        self.label_55 = QLabel(self.groupBox)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_55, 6, 0, 1, 2)

        self.label_56 = QLabel(self.groupBox)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_5.addWidget(self.label_56, 1, 0, 1, 1)

        self.label_57 = QLabel(self.groupBox)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_5.addWidget(self.label_57, 8, 0, 1, 2)


        self.verticalLayout_5.addLayout(self.gridLayout_5)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Algoritmos de paginaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RAM - OPT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RAM - Other", None))
        self.optGroupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MMU - OPT", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PAGE ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOADED", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"L-ADDR", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"M-ADDR", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"D-ADDR", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"LOADED-T", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"MARK", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"V-RAM %:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"PAGES", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"V-RAM KB:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"UNLOADED:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"seconds", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Sim-Time:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"LOADED:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RAM KB:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"RAM %:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Thrashing", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Processes:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fragmentaci\u00f3n:", None))
        self.groupBox.setTitle("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"MMU - Other", None))
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"PAGE ID", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"LOADED", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"L-ADDR", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"M-ADDR", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"D-ADDR", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"LOADED-T", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"MARK", None));
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"V-RAM %:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"PAGES", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"V-RAM KB:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"UNLOADED:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"seconds", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Sim-Time:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"LOADED:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"RAM KB:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"RAM %:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Thrashing", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Processes:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Fragmentaci\u00f3n:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
    # retranslateUi

