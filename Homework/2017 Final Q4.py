from LinkedBinaryTree import *

def is_size_tree(bin_tree):
    
    
    def is_size_tree_helper(root):
        if root is None:
            return (0, True)
        
        left_size, is_left_tree = is_size_tree_helper(root.left)
        right_size, is_right_tree = is_size_tree_helper(root.right)

        total_size = 1 +left_size+right_size

        return is_left_tree and is_right_tree and (root.data == total_size)
    

    return is_size_tree_helper(bin_tree.root)[1]
