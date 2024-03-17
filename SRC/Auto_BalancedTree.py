from PyQt5.QtWidgets import QMainWindow, QLineEdit, QWidget,  QHeaderView, QTableWidgetItem, QApplication, QComboBox, QDateEdit, QVBoxLayout, QStackedWidget, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPalette, QColor, QDesktopServices
from Tree import Tree 
import os
import sys

class BalancedTreeWg(QMainWindow):
    def __init__(self) -> None:
        super(BalancedTreeWg,self).__init__()
        uic.loadUi("Auto_BalancedTree.ui",self)
        self.click_posicion = None
        self.showMaximized()
        self.page = None
        
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
        
        #Asignación de funciones a los botones
        self.Agree.clicked.connect(Tree._Insert_New_node)
        self.Deleted.clicked.connect(Tree._Deleted_Node)
        self.Buscar.clicked.connect(Tree._Search_Node)
        self.Search.clicked.connect(Tree._Search_Nodes)
        self.Recorrer.clicked.connect(Tree.levels)
        
        #Agregando funciones a las QComboBox
       

        Cat_2 = self.Categoria_2.currentText()
        Cat_3 = self.Categoria_3.currentText()
        
        self.Categoria.currentIndexChanged.connect(self.agregar_archivos)
        self.Categoria_1.currentIndexChanged.connect(self.agregar_archivos_1)
        self.Categoria_3.currentIndexChanged.connect(self.agregar_archivos_2)
        self.Categoria_3.currentIndexChanged.connect(self.agregar_archivos_3)
        
    def go_to_page1(self)->None:
        self.stackedWidget.setCurrentIndex(0)
        
    def go_to_page2(self)->None:
        self.stackedWidget.setCurrentIndex(1) 
    
    def go_to_page3(self)->None:
        self.stackedWidget.setCurrentIndex(2)   
    
    def go_to_page4(self)->None:
        self.stackedWidget.setCurrentIndex(3)   
        
    def go_to_page5(self)->None:
        self.stackedWidget.setCurrentIndex(4) 
    
    def go_to_page6(self)->None:
        self.stackedWidget.setCurrentIndex(5)  
        
    def agregar_archivos(self)->None:
        Cat = self.Categoria.currentText()
        r_fin = self.encontrar_ruta(Cat)
        lista_archivos = self.encontrar_archivos(r_fin)
        self.Imagenes.clear()
        self.Imagenes.addItems(lista_archivos)
    
    def agregar_archivos_1(self)->None:
        Cat_1 = self.Categoria_1.currentText()
        r_fin = self.encontrar_ruta(Cat_1)
        lista_archivos = self.encontrar_archivos(r_fin)
        self.Imagen_1.clear()
        self.Imagen_1.addItems(lista_archivos) 
        
    def agregar_archivos_2(self)->None:
        Cat_2 = self.Categoria_2.currentText()
        r_fin = self.encontrar_ruta(Cat_2)
        lista_archivos = self.encontrar_archivos(r_fin)
        self.Imagen_2.clear()
        self.Imagen_2.addItems(lista_archivos)
        
    def agregar_archivos_3(self)->None:
        Cat_3 = self.Categoria_3.currentText()
        r_fin = self.encontrar_ruta(Cat_3)
        lista_archivos = self.encontrar_archivos(r_fin)
        self.Imagen_3.clear()
        self.Imagen_3.addItems(lista_archivos)

                      
        
    def encontrar_ruta(self,name_carpeta )->None:
        if name_carpeta != "Elige una opción":
        # Recorre los archivos y directorios en todo el sistema de archivos
            for root, dirs, files in os.walk('/'):
                # Verifica si el nombre de la carpeta coincide
                if name_carpeta in dirs:
                # Si encuentra la carpeta, devuelve la ruta completa
                    return os.path.join(root, name_carpeta)
    
            # Si no se encuentra la carpeta, devuelve None
            return None
        
    def encontrar_archivos(self,ruta)-> None:
        # Verifica si la ruta de la carpeta existe
        if os.path.exists(ruta) and os.path.isdir(ruta):
            # Lista para almacenar los nombres de archivos de imágenes
            nombres_imagenes = []
        
            # Itera sobre los archivos en la carpeta
            for archivo in os.listdir(ruta):
                # Verifica si el archivo es una imagen (puedes agregar más extensiones si es necesario)
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    nombres_imagenes.append(archivo)
        
            return nombres_imagenes

if __name__ == '__main__':
    app = QApplication([])
    window = BalancedTreeWg()
    window.show()
    app.exec_()
    