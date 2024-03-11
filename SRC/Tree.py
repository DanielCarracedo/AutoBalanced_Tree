from typing import Any, List, Optional, Tuple

#Creacion de la clase nodo
class Node:
    def __init__(self, data:any) -> None:
        self.left:Optional["Node"] = None
        self.right:Optional["Node"] = None
        self.data = data
   
#Creacion de la clase Tree y sus funciones       
class Tree:
    def __init__(self, root:"Node"=None) -> None:
        self.root = root
        
    def _Insert_New_node(self)->None:
        pass
    
    def _Deleted_Node(self)-> None:
        pass
    
    def _Search_Node(self)-> None:
        pass
    
    def _Search_Nodes(self)->None:
        pass
    
    def _Levels_Tree(self)-> None:
        pass
    
    def _Node_Level(self)-> None:
        pass
    
    def _Balanced_Fact(self)-> None:
        pass
    
    def _search_Father(self) -> None:
        pass
    
    def _Search_Grandpa(self)-> None:
        pass
    
    def _search_Uncle(self)-> None:
        pass
    
    