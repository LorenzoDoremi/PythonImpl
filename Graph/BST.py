

from random import random


class Nodo:
    def __init__(self, value, left, right, parent):
        self.key = value
        self.left = left
        self.right = right
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

    def add_nodo(self, key):

        self.root = self.traverse_add_nodo(self.root, key)

    def traverse_add_nodo(self, curr: Nodo, key):
        if curr is None:

            return Nodo(key, None, None, None)
        elif key > curr.key:
            if curr.right is None:
                curr.right = Nodo(key, None, None, None)
                curr.right.parent = curr
            else:
                self.traverse_add_nodo(curr.right, key)
        elif key <= curr.key:
            if curr.left is None:
                curr.left = Nodo(key, None, None, None)
                curr.left.parent = curr
            else:
                self.traverse_add_nodo(curr.left, key)
        return curr

    def in_order(self, curr):

        if curr.left is not None:
            self.in_order(curr.left)
        print(curr.key)
        if curr.right is not None:
            self.in_order(curr.right)

    def max_order(self, curr):
        if curr.right is not None:
            self.max_order(curr.right)
        print(curr.key)
        if curr.left is not None:
            self.max_order(curr.left)

  


albero = BST()
for i in range(0, 10):
    albero.add_nodo(int(random()*100))


albero.max_order(albero.root)
