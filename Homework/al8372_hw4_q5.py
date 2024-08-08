from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):

    def helper(root):
        if root is None:
            return (0, True)

        left_node = helper(root.left)
        right_node = helper(root.right)

        if left_node[0] > right_node[0]:
            height = left_node[0] + 1
        else:
            height = right_node[0] + 1
        
        balanced = left_node[1] and right_node[1] and abs(right_node[0] - left_node[0]) <= 1

        return(height, balanced)
    return helper(bin_tree.root)[1]












