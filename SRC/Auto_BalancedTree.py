from PyQt5.QtWidgets import QMainWindow, QLineEdit, QWidget,  QHeaderView, QTableWidgetItem, QApplication, QComboBox, QDateEdit, QVBoxLayout, QStackedWidget, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPalette, QColor, QDesktopServices
from Tree import Tree, Node, Queue, Stack, draw_binary_tree
import os
import sys


class BalancedTreeWg(QMainWindow):
    def __init__(self) -> None:
        super(BalancedTreeWg, self).__init__()
        uic.loadUi("Auto_BalancedTree.ui", self)
        self.click_posicion = None
        self.showMaximized()
        self.page = None
        self.tree = Tree()

        # Deshabilitar cambio de pagina por click en el QStackedWidget y que se inicie en la pagina uno
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setCurrentIndex(0)

        # Cambio de pagina por los botones deseados
        self.Inicio.clicked.connect(self.go_to_page1)
        self.New_Node.clicked.connect(self.go_to_page2)
        self.Deleted_Node.clicked.connect(self.go_to_page3)
        self.Search_Node.clicked.connect(self.go_to_page4)
        self.Search_Nodes.clicked.connect(self.go_to_page5)
        self.Levels.clicked.connect(self.go_to_page6)

        # Asignación de funciones a los botones
        self.Agree.clicked.connect(self.insertar_nodo)
        self.Deleted.clicked.connect(self.eliminar_nodo)
        """self.Buscar.clicked.connect(Tree._Search_Node)
        self.Search.clicked.connect(Tree._Search_Nodes)
        self.Recorrer.clicked.connect(Tree.levels)"""

        # Agregando funciones a las QComboBox

        Cat_2 = self.Categoria_2.currentText()
        Cat_3 = self.Categoria_3.currentText()

        self.Categoria.currentIndexChanged.connect(self.agregar_archivos)
        self.Categoria_1.currentIndexChanged.connect(self.agregar_archivos_1)
        self.Categoria_3.currentIndexChanged.connect(self.agregar_archivos_2)
        self.Categoria_3.currentIndexChanged.connect(self.agregar_archivos_3)

    def go_to_page1(self) -> None:
        # principal
        self.stackedWidget.setCurrentIndex(0)

    def go_to_page2(self) -> None:
        self.stackedWidget.setCurrentIndex(1)

    def go_to_page3(self) -> None:
        # eliminar nodo
        self.stackedWidget.setCurrentIndex(2)

    def go_to_page4(self) -> None:
        # buscar nodo
        self.stackedWidget.setCurrentIndex(3)

    def go_to_page5(self) -> None:
        # buscar nodo especifico
        self.stackedWidget.setCurrentIndex(4)

    def go_to_page6(self) -> None:
        # recorrido por niveles
        self.stackedWidget.setCurrentIndex(5)

    def agregar_archivos(self) -> None:
        Cat = self.Categoria.currentText()
        lista_archivos = self.encontrar_archivos(Cat)
        self.Imagenes.clear()
        self.Imagenes.addItems(lista_archivos)

    def agregar_archivos_1(self) -> None:
        Cat_1 = self.Categoria_1.currentText()
        lista_archivos = self.encontrar_archivos(Cat_1)
        self.Imagen_1.clear()
        self.Imagen_1.addItems(lista_archivos)

    def agregar_archivos_2(self) -> None:
        Cat_2 = self.Categoria_2.currentText()
        lista_archivos = self.encontrar_archivos(Cat_2)
        self.Imagen_2.clear()
        self.Imagen_2.addItems(lista_archivos)

    def agregar_archivos_3(self) -> None:
        Cat_3 = self.Categoria_3.currentText()
        lista_archivos = self.encontrar_archivos(Cat_3)
        self.Imagen_3.clear()
        self.Imagen_3.addItems(lista_archivos)

    def encontrar_archivos(self, name_carpeta) -> None:
        ruta_act = os.path.dirname(os.path.abspath(__file__))
        ruta_obj = os.path.join(ruta_act, name_carpeta)
        # Lista para almacenar los nombres de archivos de imágenes
        archivos = []
        # Obtener una lista de todos los elementos en la ruta especificada
        elementos = os.listdir(ruta_obj)
        for elemento in elementos:
            # Comprobar si el elemento es un archivo
            archivos.append(elemento)
        return archivos

    def insertar_nodo(self):
        dato = self.Imagenes.currentText()
        self.tree._Insert_New_node(dato)
        draw_binary_tree(self.tree.root, "arbol")
        self.go_to_page1()

    def eliminar_nodo(self, dato):
        dato = self.Imagen_1.currentText()
        self.tree.Delete_Node(dato)
        draw_binary_tree(self.tree.root, "arbol")
        self.go_to_page1()


if __name__ == '__main__':
    app = QApplication([])
    window = BalancedTreeWg()
    window.show()
    app.exec_()
