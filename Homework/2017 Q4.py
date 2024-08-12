def is_sum_balanced(bin_tree):
    # If the tree is empty, it is considered balanced.
    if bin_tree.is_empty():
        return True
    # Check if the tree rooted at the root is sum-balanced.
    return is_subtree_sum_balanced(bin_tree.root)[1]

def is_subtree_sum_balanced(root):
    # Base case: if the node is a leaf, it is balanced, and the sum is its own value.
    if root is None:
        return (0, True)
    
    # Recursively calculate the sum and check balance for left and right subtrees.
    left_sum, left_balanced = is_subtree_sum_balanced(root.left)
    right_sum, right_balanced = is_subtree_sum_balanced(root.right)
    
    # Calculate the total sum for the current subtree.
    total_sum = root.data + left_sum + right_sum
    
    # Check if the current subtree is balanced.
    is_balanced = abs(left_sum - right_sum) <= 1
    
    # The current subtree is balanced if both subtrees are balanced and the current node is balanced.
    return (total_sum, left_balanced and right_balanced and is_balanced)