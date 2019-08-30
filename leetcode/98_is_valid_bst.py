from utils import TreeNode, deserialize_tree


def is_valid_bst(root):
    stack = []
    pre = -float('inf')
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            if root.val <= pre:
                return False
            else:
                pre = root.val
            root = root.right
    return True


if __name__ == '__main__':
    bst1 = "2,1,$,$,3,$,$"
    print(is_valid_bst(deserialize_tree(bst1)))
    bst2 = "5,1,$,$,4,3,$,$,6,$,$"
    print(is_valid_bst(deserialize_tree(bst2)))
