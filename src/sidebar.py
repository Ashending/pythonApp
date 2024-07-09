from ui_menu_personal import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Side Bar")

        self.expanded_bar_widget.setHidden(True)

        self.col_dashboard.clicked.connect(self.switch_to_dashboard)
        self.exp_dashboard.clicked.connect(self.switch_to_dashboard)

        self.col_gestion.clicked.connect(self.switch_to_gestion)
        self.exp_gestion.clicked.connect(self.switch_to_gestion)

        self.col_listado.clicked.connect(self.switch_to_listado)
        self.exp_listado.clicked.connect(self.switch_to_listado)


    def switch_to_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_gestion(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_listado(self):
        self.stackedWidget.setCurrentIndex(2)

