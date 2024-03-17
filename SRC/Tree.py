from typing import Any, List, Optional, Tuple
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
# Creacion de la clase nodo


class Queue:

    def __init__(self) -> None:
        self.queue: List[Any] = []

    def add(self, elem: Any) -> None:
        self.queue.append(elem)

    def remove(self) -> Any:
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.queue) == 0


class Stack:

    def __init__(self) -> None:
        self.stack: List[Any] = []

    def add(self, elem: Any) -> None:
        self.stack.append(elem)

    def remove(self) -> Any:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self.remove()


class Node:
    def __init__(self, data: any) -> None:
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.data = data

# Creacion de la clase Tree y sus funciones


class Tree:
    def __init__(self, root: "Node" = None) -> None:
        self.root = root

    def srr(self, node) -> Node:
        aux = node.left
        node.left = aux.right
        aux.right = node
        if node.data == self.root.data:
            self.root = aux
        father = self.search_Father(node.data)
        if father.left is not None:
            if father.right.data == node.data:
                father.right = aux
        if father.right is not None:
            if father.left.data == node.data:
                father.left = aux

    def slr(self, node) -> Node:
        aux = node.right
        node.right = aux.left
        aux.left = node
        father = self.search_Father(node.data)
        if node.data == self.root.data:
            self.root = aux
        if father is not None:
            if father.left is not None:
                if father.right.data == node.data:
                    father.right = aux
            if father.right is not None:
                if father.left.data == node.data:
                    father.left = aux

    def dlrr(self, node) -> Node:
        aux = node.left.right
        node.left.right = aux.left
        aux.left = node.left
        if node.left.data == self.root.data:
            self.root = aux
        node.left = aux
        self.srr(node)

    def drlr(self, node) -> Node:
        aux = node.right.left
        node.right.left = aux.right
        aux.right = node.right
        if node.right.data == self.root.data:
            self.root = aux
        node.right = aux
        self.slr(node)

    def height(self, node):
        if node is None:
            return 0

        queue = deque()
        queue.append((node, 1))
        max_level = 0

        while queue:
            current_node, level = queue.popleft()
            max_level = max(max_level, level)
            # Agregar los nodos hijos a la cola si existen

            if current_node.left:
                queue.append((current_node.left, level + 1))
            if current_node.right:
                queue.append((current_node.right, level + 1))

        return max_level

    def balance_factor(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return right_height - left_height

    def rebalance(self, node):
        balance = self.balance_factor(node)
        leftbalance = self.balance_factor(node.left)
        rightbalance = self.balance_factor(node.right)
        """print(f"{balance} {node.data}")
        print(f"{leftbalance} l")
        print(f"{rightbalance} r")"""
        if balance == 2 and rightbalance == 0:
            print("conflicto 2")
            return self.slr(node)

        if balance == -2 and leftbalance == 0:
            print("conflicto -2")
            return self.srr(node)

        if balance > 1 and rightbalance > 0:
            print("slr")
            return self.slr(node)

        if balance < -1 and leftbalance < 0:
            print("srr")
            return self.srr(node)

        if balance < -1 and leftbalance > 0:
            print("dlrr")
            return self.dlrr(node)

        if balance > 1 and rightbalance < 0:
            print("drlr")
            return self.drlr(node)

        return node

    def rebalance_tree(self, node):
        path = Queue()
        current = node
        while current is not None:
            path.add(current)
            current = self.search_Father(current.data)

        while not path.is_empty():
            node = path.remove()
            node = self.rebalance(node)

    def find_predecessor(self, node):
        if node.left is not None:
            return self._max_value(node.left)
        else:
            pred = None
            current = self.root
            while current is not None:
                if node.key < current.key:
                    current = current.left
                elif node.key > current.key:
                    pred = current
                    current = current.right
                else:
                    break
            return pred

    def _max_value(self, node):
        while node.right is not None:
            node = node.right
        return node

    def search_node(self, node):
        p = self.root
        s = Stack()
        while (p is not None or not s.is_empty()):
            if p is not None:
                if p.data == node:
                    return p
                else:
                    s.add(p)
                    p = p.left
            else:
                p = s.remove()
                p = p.right

    def Delete_Node(self, node) -> None:
        node = self.search_node(node)
        if node is not None:
            if node.right is not None and node.left is not None:
                predecessor = self.find_predecessor(node)
                father = self.search_Father(predecessor.data)
                if predecessor.left is None:
                    node.data = predecessor.data
                    if father.right == predecessor:
                        father.right = None
                    else:
                        father.left = None
                else:
                    node.data = predecessor.data
                    if father.right == predecessor:
                        father.right = predecessor.left
                    else:
                        father.left = predecessor.left
            elif node.right is not None or node.left is not None:
                father = self.search_Father(node.data)
                if node.left is not None:
                    if father.left == node:
                        father.left = node.left
                    else:
                        father.right = node.left
                elif node.right is not None:
                    if father.left == node:
                        father.left = node.right
                    else:
                        father.right = node.right
            else:
                father = self.search_Father(node.data)
                if father.left == node:
                    father.left = None
                else:
                    father.right = None
        self.rebalance_tree(father)

    def search_Father(self, data_s: Any) -> None:
        p, pad = self.root, None
        s, flag = Stack(), False
        while (p is not None or not s.is_empty()) and not flag:
            if p is not None:
                if p.data == data_s:
                    if pad is not None:
                        return pad
                    flag = True
                else:
                    s.add(p)
                    pad = p
                    p = p.left
            else:
                p = s.remove()
                pad = p
                p = p.right

    def _Insert_New_node(self, dato) -> None:
        dato = Node(dato)
        if self.root is None:
            self.root = dato
            return True

        p = self.search_node(dato)
        stack = Stack()
        current = self.root
        if p is None:
            while current:
                if dato.data < current.data:
                    if current.left is None:
                        current.left = dato
                        self.rebalance_tree(dato)
                        return True
                    else:
                        current = current.left
                elif dato.data > current.data:
                    if current.right is None:
                        current.right = dato
                        self.rebalance_tree(dato)
                        return True
                    else:
                        current = current.right

        return False

    def _Search_Node(self) -> None:
        pass

    def _Search_Nodes(self) -> None:
        pass

    def _Levels_Tree(self) -> None:
        pass

    def _Node_Level(self) -> None:
        pass

    def _Search_Grandpa(self) -> None:
        pass

    def _search_Uncle(self) -> None:
        pass

    def levels_nr(self) -> None:
        p, q = self.root, Queue()
        q.add(p)
        while not q.is_empty():
            p = q.remove()
            print(p.data, end=' ')
            if p.left is not None:
                q.add(p.left)
            if p.right is not None:
                q.add(p.right)


def generate_sample_abb():
    T = Tree(Node('A'))
    T.root.left = Node('B')
    T.root.right = Node('C')
    T.root.left.left = Node('D')
    T.root.left.right = Node('E')
    T.root.right.right = Node('F')
    T.root.left.left.left = Node('G')
    T.root.left.left.right = Node('H')
    T.root.right.right.left = Node('I')
    T.root.right.right.right = Node('J')
    T.root.right.left = Node('K')

    return T


def draw_binary_tree(root, filename):
    G = nx.Graph()

    def add_edges(node, pos=None, level=0, max_level=None):
        if max_level is not None and level > max_level:
            return
        if pos is None:
            pos = (0, 0)
        G.add_node(node.data, pos=pos)
        if node.left:
            new_pos = (pos[0] - 1 / 2 ** level, pos[1] - 1)
            G.add_edge(node.data, node.left.data)
            add_edges(node.left, pos=new_pos,
                      level=level + 1, max_level=max_level)
        if node.right:
            new_pos = (pos[0] + 1 / 2 ** level, pos[1] - 1)
            G.add_edge(node.data, node.right.data)
            add_edges(node.right, pos=new_pos,
                      level=level + 1, max_level=max_level)

    add_edges(root)

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_size=700,
            node_color="skyblue", font_size=10)
    plt.savefig(filename)  # Guarda el árbol como imagen
    plt.close()  # Cierra la figura para liberar memoria


"""T = generate_sample_abb()
T.levels_nr()
T.Delete_Node("G")
print("\n")
T.levels_nr()
T.Delete_Node("E")
T.levels_nr()"""

T = Tree()
T._Insert_New_node(10)
T._Insert_New_node(8)
T._Insert_New_node(12)
T._Insert_New_node(9)
T._Insert_New_node(11)
T._Insert_New_node(7)
T._Insert_New_node(13)
T._Insert_New_node(15)
T._Insert_New_node(14)
T.Delete_Node(15)
T.levels_nr()
print("\n")
T.Delete_Node(11)
T.Delete_Node(9)
T.levels_nr()

draw_binary_tree(T.root, "binary_tree.png")
