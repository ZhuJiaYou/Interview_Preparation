def get_next(node):
    if node is None:
        return None
    if node.right:
        pre = node.right
        while pre.left:
            pre = pre.left
    while node.parent:
        pt = node.parent
        if pt.left == node:
            return pt
        node = pt
    return None
