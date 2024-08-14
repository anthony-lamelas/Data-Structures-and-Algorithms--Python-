
from ArrayStack import *
class SimpleTree:
    def __init__(self, element, left=None, right=None, parent=None):
        self.element = element
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.element)

    def pre_order_print(root):
        s = ArrayStack()

        s.push(root.data)

        while len(s) > 0:
            top = s.pop()
            print(top.data)
            if top.right is not None:
                s.push(top.right)
            if top.left is not None:
                s.push(root.left)

    



    