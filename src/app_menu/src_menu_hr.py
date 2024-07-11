import mysql.connector
from app_menu.menu_hr import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QHBoxLayout, QWidget

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="192.168.187.128",
            user="lilbirbo",
            database="taller",
            password="lilbirbo01#"
        )
        self.cursor = self.mydb.cursor(dictionary=True)

class MenuHR(QMainWindow, Ui_MainWindow):
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

        query = "SELECT * FROM `trabajador`;"
        db = Database()
        db.cursor.execute(query)
        self.load_tabla_trabajadores(db.cursor.fetchall())


    def switch_to_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_gestion(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_listado(self):
        self.stackedWidget.setCurrentIndex(2)

    def load_tabla_trabajadores(self, data):
        self.tabla_trabajadores.setRowCount(0)

        for row_index, row_data in enumerate(data):
            self.tabla_trabajadores.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tabla_trabajadores.setItem(row_index, col_index, item)

                double_button_widget = DoubleButtonWidget(row_index, row_data)

                self.tabla_trabajadores.setCellWidget(row_index, 10, double_button_widget)
                self.tabla_trabajadores.setRowHeight(row_index, 50, double_button_widget)


class DoubleButtonWidget(QWidget):
    def __init__(self, row, row_data):
        super().__init__()
        self.row_index = row
        self.row_data = row_data

        self.rut_trabajador = self.row_data[0]
        self.nombre_trabajador = self.row_data[1]

        layout = QHBoxLayout(self)
        self.boton_editar = QPushButton("", self)
        self.boton_editar.setStyleSheet("background-color: rgb(74, 154, 181);")
        self.boton_editar.setFixedSize(61, 31)

        self.boton_eliminar = QPushButton("", self)
        self.boton_eliminar.setStyleSheet("background-color: rgb(178, 70, 87);")
        self.boton_eliminar.setFixedSize(61, 31)

        icono_editar = QIcon("../../resources/icons/pencil.png")
        self.boton_editar.setIcon(icono_editar)

        icono_eliminar = QIcon("../../resources/icons/cross.png")
        self.boton_eliminar.setIcon(icono_eliminar)

