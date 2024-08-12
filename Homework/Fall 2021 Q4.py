from LinkedBinaryTree import *

def distribution_of_leaves_by_parity(root):
    if root is None:
        return (0,0)
    
    if root.right is None and root.left is None:
        if root.data % 2 == 0:
            return (1,0)
        else:
            return (0,1)
        
    lefte, lefto = distribution_of_leaves_by_parity(root.left)
    righte, righto = distribution_of_leaves_by_parity(root.right)

    even_count = lefte + righte
    odd_count = lefto + righto

    
    

    return(even_count, odd_count)
            