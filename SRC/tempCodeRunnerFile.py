    # Borra el texto anterior antes de agregar el nuevo texto
        self.Recorrido.clear()

        # La variable L recibe la lista de listas que contiene los datos y los niveles de los nodos
        L = self.tree._Levels_Tree_r(self.tree.root, level=0, levels=[])

        # Recorre la lista de niveles y nodos
        for i in range(len(L)):
            for j in range(len(L)):
                # Si el nivel del nodo es igual al nivel actual, agrega el nodo al QTextEdit
                if L[j][1] == i:
                    self.Recorrido.insertPlainText(L[j][0] + " ")