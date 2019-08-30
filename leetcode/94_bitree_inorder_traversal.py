from utils import TreeNode, deserialize_tree


def inorder_traversal(root):
    stack = []
    traversal = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            traversal.append(root.val)
            root = root.right
    return traversal


if __name__ == '__main__':
    t1 = '1,$,2,3,$,$,$'
    t1 = deserialize_tree(t1)
    print(inorder_traversal(t1))

