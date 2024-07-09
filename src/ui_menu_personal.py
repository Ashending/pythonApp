# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_personal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import rc_menu_personal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 685)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 241, 237);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.colapsed_bar_widget = QWidget(self.centralwidget)
        self.colapsed_bar_widget.setObjectName(u"colapsed_bar_widget")
        self.colapsed_bar_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(85, 170, 127);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 30px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color: rgb(220, 255, 236);\n"
"	color: rgb(85, 170, 127);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.colapsed_bar_widget)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.colapsed_bar_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u":/icons/home.png"))

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.col_dashboard = QPushButton(self.colapsed_bar_widget)
        self.col_dashboard.setObjectName(u"col_dashboard")
        icon = QIcon()
        icon.addFile(u":/icons/dashboard_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.col_dashboard.setIcon(icon)
        self.col_dashboard.setCheckable(True)
        self.col_dashboard.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.col_dashboard)

        self.col_gestion = QPushButton(self.colapsed_bar_widget)
        self.col_gestion.setObjectName(u"col_gestion")
        icon1 = QIcon()
        icon1.addFile(u":/icons/users-alt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.col_gestion.setIcon(icon1)
        self.col_gestion.setCheckable(True)
        self.col_gestion.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.col_gestion)

        self.col_listado = QPushButton(self.colapsed_bar_widget)
        self.col_listado.setObjectName(u"col_listado")
        icon2 = QIcon()
        icon2.addFile(u":/icons/list-check.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.col_listado.setIcon(icon2)
        self.col_listado.setCheckable(True)
        self.col_listado.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.col_listado)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 419, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_7 = QPushButton(self.colapsed_bar_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon3 = QIcon()
        icon3.addFile(u":/icons/log_out_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.colapsed_bar_widget, 0, 0, 1, 1)

        self.expanded_bar_widget = QWidget(self.centralwidget)
        self.expanded_bar_widget.setObjectName(u"expanded_bar_widget")
        self.expanded_bar_widget.setMaximumSize(QSize(200, 16777215))
        self.expanded_bar_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(85, 170, 127);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: white;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color: rgb(220, 255, 236);\n"
"	color: rgb(85, 170, 127);\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.expanded_bar_widget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.expanded_bar_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setPixmap(QPixmap(u":/icons/home.png"))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.expanded_bar_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.exp_dashboard = QPushButton(self.expanded_bar_widget)
        self.exp_dashboard.setObjectName(u"exp_dashboard")
        self.exp_dashboard.setIcon(icon)
        self.exp_dashboard.setCheckable(True)
        self.exp_dashboard.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.exp_dashboard)

        self.exp_gestion = QPushButton(self.expanded_bar_widget)
        self.exp_gestion.setObjectName(u"exp_gestion")
        self.exp_gestion.setIcon(icon1)
        self.exp_gestion.setCheckable(True)
        self.exp_gestion.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.exp_gestion)

        self.exp_listado = QPushButton(self.expanded_bar_widget)
        self.exp_listado.setObjectName(u"exp_listado")
        self.exp_listado.setIcon(icon2)
        self.exp_listado.setCheckable(True)
        self.exp_listado.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.exp_listado)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 418, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_8 = QPushButton(self.expanded_bar_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.expanded_bar_widget, 0, 1, 1, 1)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.verticalLayout_5 = QVBoxLayout(self.main_screen_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.main_screen_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu = QPushButton(self.widget)
        self.menu.setObjectName(u"menu")
        icon4 = QIcon()
        icon4.addFile(u":/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon4)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(538, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon5 = QIcon()
        icon5.addFile(u":/icons/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QSize(20, 20))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.pushButton_10)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.stackedWidget.addWidget(self.dashboard)
        self.listado = QWidget()
        self.listado.setObjectName(u"listado")
        self.stackedWidget.addWidget(self.listado)
        self.opciones = QWidget()
        self.opciones.setObjectName(u"opciones")
        self.stackedWidget.addWidget(self.opciones)
        self.gestion = QWidget()
        self.gestion.setObjectName(u"gestion")
        self.stackedWidget.addWidget(self.gestion)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_screen_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.colapsed_bar_widget.setHidden)
        self.menu.toggled.connect(self.expanded_bar_widget.setVisible)
        self.col_listado.toggled.connect(self.exp_listado.setChecked)
        self.col_gestion.toggled.connect(self.exp_gestion.setChecked)
        self.col_dashboard.toggled.connect(self.exp_dashboard.setChecked)
        self.exp_dashboard.toggled.connect(self.col_dashboard.setChecked)
        self.exp_gestion.toggled.connect(self.col_gestion.setChecked)
        self.exp_listado.toggled.connect(self.col_listado.setChecked)
        self.pushButton_7.toggled.connect(MainWindow.close)
        self.pushButton_8.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.col_dashboard.setText("")
        self.col_gestion.setText("")
        self.col_listado.setText("")
        self.pushButton_7.setText("")
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.exp_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.exp_gestion.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.exp_listado.setText(QCoreApplication.translate("MainWindow", u"Listado", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.menu.setText("")
        self.pushButton_10.setText("")
    # retranslateUi

