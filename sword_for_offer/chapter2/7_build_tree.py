from utils import TreeNode, preorder_traversal, inorder_traversal


def buildTree(preorder: 'list[int]', inorder: 'list[int]') -> TreeNode:
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree(preorder, inorder[0:ind])
        root.right = buildTree(preorder, inorder[ind+1:])
        return root


def buildTree2(preorder: 'list[int]', inorder: 'list[int]') -> TreeNode:
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
    preorder.reverse()
    inorder.reverse()
    return build(None)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    t1 = buildTree2(preorder.copy(), inorder.copy())
    print("{0} --- {1}".format(preorder_traversal(t1), preorder))
    print("{0} --- {1}".format(inorder_traversal(t1), inorder))
