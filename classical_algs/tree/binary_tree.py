class BinaryNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_traverse(root):
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def pre_traverse_no_recur(root):
    if root == None:
        return
    rights = []

    pos = root
    while (pos != None) or (len(rights) > 0):
        if pos == None:
            pos = rights.pop()
        else:
            print(pos.value)
            rights.append(pos.right)
            pos = pos.left


def post_traverse(root):
    if root == None:
        return
    post_traverse(root.left)
    post_traverse(root.right)
    print(root.value, end=" ")


def post_traverse_no_recur(root):
    if root == None:
        return
    fathers = []
    pos = root
    last = None
    fathers.append(root)
    while (pos != None) or (len(fathers) > 0):
        if pos == None:
            pos = fathers.pop()
        else:
            if (pos.left == None) and (pos.right == None):
                print(pos.value)
                last = pos
                pos = None
            elif (pos.left != None) and (pos.right != None):
                if last == pos.right:
                    print(pos.value)
                    last = pos
                    pos = None
                elif last == pos.left:
                    pos = pos.right
                else:
                    fathers.append(pos)
                    pos = pos.left
            elif pos.left != None:
                if last == pos.left:
                    print(pos.value)
                    last = pos
                    pos = None
                else:
                    fathers.append(pos)
                    pos = pos.left
            else:
                if last == pos.right:
                    print(pos.value)
                    last = pos
                    pos = None
                else:
                    fathers.append(pos)
                    pos = pos.right


def post_traverse_no_recur2(root):
    if root == None:
        return
    stack = list()
    stack.append(root)
    stack.append(root)
    pos = root
    while len(stack) > 0:
        pos = stack.pop()
        if (len(stack) > 0) and (pos == stack[-1]):
            if pos.right != None:
                stack.append(pos.right)
                stack.append(pos.right)
            if pos.left != None:
                stack.append(pos.left)
                stack.append(pos.left)
        else:
            print(pos.value, end=" ")


def mid_traverse(root):
    if root == None:
        return
    mid_traverse(root.left)
    print(root.value, end=" ")
    mid_traverse(root.right)


def mid_traverse_no_recur(root):
    if not root:
        return
    p = root
    stack = []
    while p or stack:
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            print(p.value, end=" ")
            p = p.right


if __name__ == '__main__':
    root = BinaryNode('a', BinaryNode('b', BinaryNode('c'), BinaryNode('d')), 
            BinaryNode('e', BinaryNode('f', None, BinaryNode('g'))))

    mid_traverse(root)
    print()
    mid_traverse_no_recur(root)
