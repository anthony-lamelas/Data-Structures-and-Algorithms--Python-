from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    if not bin_tree:
        raise Exception('Empty Tree')
    
    node = bin_tree.root
    
    def subtree_min_and_max(root):
        if root is None:
            return None, None
        
        left_min, left_max = subtree_min_and_max(root.left)
        right_min, right_max = subtree_min_and_max(root.right)
       
        min_val = root.data
        max_val = root.data

        if left_min is not None:
            if left_min < min_val:
                min_val = left_min
        if left_max is not None:
            if left_max > max_val:
                max_val = left_max
                
        if right_min is not None:
            if right_min < min_val:
                min_val = right_min
        if right_max is not None:
            if right_max > max_val:
                max_val = right_max

        return min_val, max_val
        
    return subtree_min_and_max(node)     



