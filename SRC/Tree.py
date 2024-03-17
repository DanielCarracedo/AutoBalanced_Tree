from typing import Any, List, Optional, Tuple
from collections import deque

# Creacion de la clase nodo


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self.pop()


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
        return aux

    def slr(self, node) -> Node:
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux

    def dlrr(self, node) -> Node:
        node.left = self.slr(node.left)
        return self.srr(node)

    def drlr(self, node) -> Node:
        node.right = self.srr(node.right)
        return self.slr(node)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            return max(left_height, right_height) + 1

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.right) - self.height(node.left)

    def rebalance(self, node):
        balance = self.balance_factor(node)
        leftbalance = self.balance_factor(node.left)
        rightbalance = self.balance_factor(node.right)

        if balance > 1 and rightbalance > 0:
            return self.slr(node)

        if balance < -1 and leftbalance < 0:
            return self.srr(node)

        if balance > 2 and rightbalance < 0:
            return self.dlrr(node)

        if balance < -1 and leftbalance > 0:
            return self.drlr(node)

        return node

    def rebalance_tree(self, node):
        path = Stack()
        current = node
        while current is not None:
            path.push(current)
            current = self.search_Father(current)

        # Rebalance all nodes along the path
        for node in path:
            node = self.rebalance(node)

    def find_predecessor(self, node):
        pass

    def Delete_Node(self, node) -> None:
        if node.right is not None and node.left is not None:
            predecessor = self.find_predecessor()
            father = self.search_Father(predecessor)
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
            father = self.search_Father(node)
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
            father = self.search_Father(node)
            if father.left == node:
                father.left = None
            else:
                father.right = None

        self.rebalance_tree()

    def search_Father(self, data_s: Any) -> None:
        p, pad = self.root, None
        s, flag = Stack(), False
        while (p is not None or not s.is_empty()) and not flag:
            if p is not None:
                if p.data == data_s:
                    if pad is not None:
                        print(f'El padre de {data_s!r} es {pad.data!r}')
                    flag = True
                else:
                    s.add(p)
                    pad = p
                    p = p.left
            else:
                p = s.remove()
                pad = p
                p = p.right

        if not flag or pad is None:
            print(f'Para {data_s!r} no hay padre')

    def _Insert_New_node(self) -> None:
        pass

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
