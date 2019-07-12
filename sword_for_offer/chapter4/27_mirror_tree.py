from utils import deserialize_tree, TreeNode, is_same_tree


def mirror_tree(root):
    if root:
        mirror_tree(root.left)
        mirror_tree(root.right)
        root.left, root.right = root.right, root.left
    return root


if __name__ == '__main__':
    t1 = '8,6,5,$,$,7,$,$,10,9,$,$,11,$,$'
    t2 = '8,10,11,$,$,9,$,$,6,7,$,$,5,$,$'
    t1 = deserialize_tree(t1)
    t2 = deserialize_tree(t2)
    print(is_same_tree(t2, mirror_tree(t1)))
