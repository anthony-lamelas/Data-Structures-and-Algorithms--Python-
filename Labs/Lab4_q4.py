from LinkedBinaryTree import LinkedBinaryTree

def bt_even_sum(root):
    if root is None:
        return 0
    
    current_value = root.value if root.value % 2 == 0 else 0

    left = bt_even_sum(root.left)
    right = bt_even_sum(root.right)

    return current_value +left+right

def bt_contains(root, val):

    
