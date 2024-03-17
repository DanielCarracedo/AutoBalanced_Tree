from typing import Any, List, Optional, Tuple

#Creacion de la clase nodo
class Node:
    def __init__(self, data:any, category:str) -> None:
        self.left:Optional["Node"] = None
        self.right:Optional["Node"] = None
        self.data = data
        self.category = category
   
#Creacion de la clase Tree y sus funciones       
class Tree:
    def __init__(self, root:"Node"=None) -> None:
        self.root = root
        
    #Todos
    def _Insert_New_node(self)->None:
        pass
    
    #Jose
    def _Deleted_Node(self)-> None:
        pass
    
    #Ya
    def _Search_Node(self)-> None:
        pass
    
    #Franche
    def _Search_Nodes(self)->None:
        pass
    
    #Funcion auxiliar para imprimir el recorrido por niveles
    def levels(self)->None:
        
        #La variable L recibe la lista de listas que contiene los datos y los niveles de los nodos
        L =self.levels_r(self.root)
              
        #El primer for representa el nivel en el que nos encontramos
        for i in range(len(L)):
            
            #El segundo  representa la lista en la que nos encontramos
            for j in range(len(L)):
                
                #La condicion es que si el nivel del nodo de la lista en la posicion j es igual al nivel
                #en el que nos encontramos entonces lo imprimimos 
                if L[j][1] == i:
    
                    print(L[j][0], end= " ")
                    
    def _Levels_Tree_r(self,node:"Node",level=0,levels=[])-> None:
        if node is not None:
            levels.append([node.data,level])
            if node.left is not None:
                self.levels_r(node.left,level + 1)
            if node.right is not None:
                self.levels_r(node.right, level + 1)
        return levels
    
    #Daniel
    def __Node_Level(self, node:"Node", elem:"Node", level = 0)-> None:
        if node is not None:
            if node.data == elem.data :
                print("El nodo " f"{elem.data}" " se encuentra en el nivel " f"{level }")
                return True
            else:
                self.__Node_Level(node.left,elem, level + 1)
                self.__Node_Level(node.right, elem, level + 1)
    
    #Jose
    def _Balanced_Fact(self)-> None:
        pass
    
    #Ya
    def _search_Father(self) -> None:
        pass
    
    #Franche
    def _Search_Grandpa(self)-> None:
        pass
    
    #Ya   
    def _search_Uncle(self)-> None:
        pass
    
    