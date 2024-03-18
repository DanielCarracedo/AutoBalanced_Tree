from PyQt5.QtWidgets import QMainWindow, QLineEdit, QWidget,  QHeaderView, QTableWidgetItem, QApplication, QComboBox, QDateEdit, QVBoxLayout, QStackedWidget, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPalette, QColor, QDesktopServices, QPixmap
from Tree import Tree, draw_binary_tree
import os


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
        self.Buscar.clicked.connect(self.search_Node)
        self.Search.clicked.connect(self.search_Nodes)
        self.Recorrer.clicked.connect(self.levels)

        # Agregando funciones a las QComboBox
        self.Categoria.currentIndexChanged.connect(self.agregar_archivos)
        self.Categoria_1.currentIndexChanged.connect(self.agregar_archivos_1)
        self.Categoria_2.currentIndexChanged.connect(self.agregar_archivos_2)
        self.Elegir.currentIndexChanged.connect(self._options)
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

    def obtener_ruta_imagen(self, nombre_imagen, directorio):
        ruta_completa = os.path.join(directorio, nombre_imagen)
        if os.path.exists(ruta_completa):
            return ruta_completa
        else:
            print(
                f"No se encontró la imagen '{nombre_imagen}' en el directorio '{directorio}'")
            return None

    def search_Nodes(self):
        pass

    def levels(self) -> None:

        # La variable L recibe la lista de listas que contiene los datos y los niveles de los nodos
        L = self.tree._Levels_Tree_r(self.tree.root)

        # El primer for representa el nivel en el que nos encontramos
        for i in range(len(L)):

            # El segundo  representa la lista en la que nos encontramos
            for j in range(len(L)):

                # La condicion es que si el nivel del nodo de la lista en la posicion j es igual al nivel
                # en el que nos encontramos entonces lo imprimimos
                if L[j][1] == i:
                    agg = self.Recorrido.text() + L[j][0]+ " "
                    self.Recorrido.setText(agg)
   
    def search_Node(self):
        find = self.Imagen_2.currentText()
        x = self.tree.search_node(find)
        y = self._options()
        agg = "El nodo "+f"{x.data}"+" "+f"{y}"
        self.Info.setText(agg)
        
    def _options(self):
        x = self.Elegir.currentText()
        find = self.Imagen_2.currentText()
        if x == "Obtener el nivel del nodo":
            l = self.tree._Node_Level(find)
            level = "El nivel del nodo es "+f"{l}"
            return level 
        elif x == "Obtener el factor de balanceo (equilibrio) del nodo":
            nodo = self.tree.search_node(find)
            f = self.tree.balance_factor(nodo) 
            fac = "El factor de balanceo  del nodo es " + f"{f}"
            return fac
        elif x== "Encontrar el padre del nodo":
            p = self.tree.search_Father(find)
            pad = "cuenta como padre padre al nodo  "+ f"{p.data}"
            return pad
        elif x == " Encontrar el abuelo del nodo":
            grand = self.tree._Search_Grandpa()
            grandpa = "todavia no pa :P"
            return grandpa
        elif x == "Encontrar el tío del nodo":
            t = self.tree._search_Uncle(self.tree.root,None,None,find)
            tio = "tiene como tio al nodo  "+f"{t.data}"
            return tio
        
    def update_image(self):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        directorio_actual = os.path.join(ruta_actual, "Image")
        ruta_imagen = self.obtener_ruta_imagen("Arbol.png", directorio_actual)
        pixmap = QPixmap(ruta_imagen)
        if not pixmap.isNull():
            self.Arbol.setPixmap(pixmap.scaled(self.Arbol.size()))
        else:
            print("Error: No se pudo cargar la imagen desde", ruta_imagen)

    def insertar_nodo(self):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_carpeta_objetivo = os.path.join(ruta_actual, "Image")
        dato = self.Imagenes.currentText()
        x = self.tree._Insert_New_node(dato)
        if not x:
            self.go_to_page1()
        else:
            draw_binary_tree(self.tree.root, ruta_carpeta_objetivo, "Arbol")
            self.update_image()
            self.go_to_page1()

    def eliminar_nodo(self, dato):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_carpeta_objetivo = os.path.join(ruta_actual, "Image")
        dato = self.Imagen_1.currentText()
        if not self.tree.search_node(dato):
            self.go_to_page1()
        else:
            self.tree.Delete_Node(dato)
            draw_binary_tree(self.tree.root, ruta_carpeta_objetivo, "Arbol")
            self.update_image()
            self.go_to_page1()


if __name__ == '__main__':
    app = QApplication([])
    window = BalancedTreeWg()
    window.show()
    app.exec_()
