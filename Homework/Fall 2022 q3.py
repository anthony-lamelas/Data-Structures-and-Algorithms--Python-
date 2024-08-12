from LinkedBinaryTree import *

def costed_height(root):
    if root.left is None and root.right is None:
        return root.data
    elif root.left is None:
        return root.data + costed_height(root.right)
    elif root.right is None:
        return root.data + costed_height(root.left)
    else:
        return root.data + max(costed_height(root.left, root.right))
    