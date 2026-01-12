# Binary Tree Implementation in Python

'''
How to use:
1. Create a binary tree by instantiating the BinaryTree class.
2. Use the insert method to add values to the tree.
3. Use the inorder_traversal method to get the values in sorted order.

Structure:
Root
 ├── Left Child
 └── Right Child

'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_rec(self.root, data)

    def _insert_rec(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_rec(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_rec(node.right, data)

    def inorder_traversal(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        res = []
        if node:
            res = self._inorder_rec(node.left)
            res.append(node.data)
            res = res + self._inorder_rec(node.right)
        return res
    
# Example usage:

if __name__ == "__main__":
    
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(2)
    bt.insert(4)
    bt.insert(6)
    bt.insert(8)

