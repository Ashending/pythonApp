from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from app_menu.src_menu_hr import MenuHR

app = QApplication(sys.argv)

window = MenuHR()
window.show()

app.exec()




