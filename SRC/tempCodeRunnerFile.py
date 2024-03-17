        if balance == 2 and rightbalance == 0:
            return self.slr(node)

        if balance == -2 and leftbalance == 0:
            return self.srr(node)