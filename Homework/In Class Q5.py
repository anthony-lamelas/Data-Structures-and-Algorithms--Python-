from LinkedBinaryTree import *

def check_BSTs(bst1, bst2):
    lst1 = [node.data for node in bst1]
    lst2 = [node.data for node in bst2]
        
    return lst1 == lst2
        

        

