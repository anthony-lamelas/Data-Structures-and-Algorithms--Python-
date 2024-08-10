from Lab5 import *

def invert_bt(root):
    if root.left is None and root.right is None:
        return None
    else:
        
        root.left, root.right = root.right, root.left
            
        if root.left:
            return invert_bt(root.left)
        elif root.right:
            return invert_bt(root.right)
        
        return root
    
def min_max_BST(bst):
    root = bst.root
    min = root.data
    max = root.data

    while root.left is not None:
        if root.left.data < min:
            min = root.left.data
        elif root.left.data > max:
            max = root.left.data
        root = root.left

    while root.right is not None:
        if root.right.data < min:
            min = root.right.data
        elif root.right.data > max:
            max = root.right.data
        root = root.right
    return(min,max)
    
    
def compare_BST(bst1, bst2):
    root1 = bst1.root
    root2 = bst2.root
    tree1 = [root1]
    tree2 = [root2]

    while root1.left is not None:
        tree1.append(root1.left.data)
        root1 = root1.left

    while root1.right is not None:
        tree1.append(root1.right.data)
        root1 = root1.right

    while root2.left is not None:
        tree2.append(root2.left.data)
        root2 = root2.left

    while root2.right is not None:
        tree2.append(root2.right.data)
        root2 = root2.right

    if tree1.sort() == tree2.sort():
        return True
    else:
        return False
    










# Create nodes
node4 = LinkedBinaryTree.Node(4)
node5 = LinkedBinaryTree.Node(5)
node6 = LinkedBinaryTree.Node(6)
node7 = LinkedBinaryTree.Node(7)
node2 = LinkedBinaryTree.Node(2, node4, node5)
node3 = LinkedBinaryTree.Node(3, node6, node7)
root = LinkedBinaryTree.Node(1, node2, node3)

# Create the tree
tree = LinkedBinaryTree(root)
tree2 = LinkedBinaryTree(root)

print(compare_BST(tree, tree2))
    

    

