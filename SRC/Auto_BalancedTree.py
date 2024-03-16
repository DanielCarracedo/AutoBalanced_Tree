from PyQt5.QtWidgets import QMainWindow, QLineEdit, QWidget,  QHeaderView, QTableWidgetItem, QApplication, QComboBox, QDateEdit, QVBoxLayout, QStackedWidget, QMessageBox
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QDate

class BalancedTreeWg(QMainWindow):
    def __init__(self) -> None:
        super().__init__(BalancedTreeWg,self).__init__()
        uic.loadUi("Auto_BalancedTree.ui",self)
        self.click_posicion = None
        self.showMaximized()
        self.page = None
        
        # Deshabilitar cambio de pagina por click en el QStackedWidget
        self.stackedWidget.setMouseTracking(False)