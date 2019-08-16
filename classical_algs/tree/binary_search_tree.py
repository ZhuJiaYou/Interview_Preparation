import random


class BinarySearchNode():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self, values=None):
        self.root = None
        random.shuffle(values)
        for value in values:
            self.root = self.insert(self.root, value)

    def insert(self, root, value):
        if root == None:
            return BinarySearchNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        return root

    def mid_traverse(self, root):
        if root == None:
            return
        self.mid_traverse(root.left)
        print(root.value)
        self.mid_traverse(root.right)

    def query(self, root, val):
        if root == None:
            return False
        if root.value == val:
            return True
        elif val < root.value:
            return self.query(root.left, val)
        else:
            return self.query(root.right, val)

    def find_min(self, root):
        if root.left == None:
            return root
        else:
            return self.find_min(root.left)
        
    def find_max(self, root):
        if root.right == None:
            return root
        else:
            return self.find_max(root.right)

    def delete_node(self, root, val):
        """
        Delete a node whose value is val in BST 
        """
        if self.query(root, val) == False:
            return
        if val < root.value:
            root.left = self.delete_node(root.left, val)
        elif val > root.value:
            root.right = self.delete_node(root.right, val)
        else:
            if (root.left != None) and (root.right != None):
                next_val = self.find_min(root.right)
                root.value = next_val
                root.right = self.delete_node(root.right, next_val)
            if (root.left == None) and (root.right == None):
                root = None
            elif root.right != None:
                root = root.right
            else:
                root = root.left
        return root
            

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    bst = BinarySearchTree(values)
    bst.delete_node(bst.root, 4)
    bst.mid_traverse(bst.root)
