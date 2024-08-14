from LinkedBinaryTree import *
from ArrayQueue import *

def max_width(tree):
    q = ArrayQueue()
    q.enqueue(tree.root)
    widths = []

    

    while not q.is_empty():
        widths.append(len(q))
        for i in range (len(q)):
            node = q.dequeue()
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return max(widths)
