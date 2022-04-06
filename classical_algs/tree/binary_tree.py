class BinaryNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_traverse(root):
    if root:
        print(root.value)
        pre_traverse(root.left)
        pre_traverse(root.right)


def pre_traverse_no_recur(root):
    r = []
    s = [root]
    while s:
        p = s.pop()
        if p:
            print(p.value)
            s.append(p.right)
            s.append(p.left)


def post_traverse(root):
    if root:
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
    stack = list()
    if root:
        stack.append(root)
        stack.append(root)
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
    if root:
        mid_traverse(root.left)
        print(root.value, end=" ")
        mid_traverse(root.right)


def mid_traverse_no_recur(root):
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.value, end=" ")
            root = root.right


def level_traverse(root):
    q = []
    if root:
        q.append(root)
    while q:
        for n in q:
            print(n.value, end=' ')
        t = []
        for i in q:
            t += [i.left, i.right]
        q = [j for j in t if j]


if __name__ == '__main__':
    root = BinaryNode('a', BinaryNode('b', BinaryNode('c'), BinaryNode('d')), 
            BinaryNode('e', BinaryNode('f', None, BinaryNode('g'))))

    mid_traverse(root)
    print()
    mid_traverse_no_recur(root)
    print()
    level_traverse(root)
