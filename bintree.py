from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
# Below is the implementation of the insertion operation using recursion.
# search from https://www.geeksforgeeks.org/insertion-in-binary-search-tree/?ref=rbp
class BST:
    def __init__(self):
        self.root = None
        self.mirrors = False

    def insert(self, key):
        self.root = self.insert_A(self.root, key)

    def insert_A(self, root, key):
        if root is None:
            return Node(key)
        #else:
            #if root.val == key:
                #return root
           # elif key < root.val:
               # root.left = self.insert_A(root.left, key)
            #elif key > root.val:
            #    root.right = self.insert_A(root.right, key)
        if ((not self.mirrors and key < root.val) or (self.mirrors and key > root.val)):
            root.left = self.insert_A(root.left, key)
        elif ((not self.mirrors and key > root.val) or (self.mirrors and key < root.val)):
            root.right = self.insert_A(root.right, key)
        return root
# Only used to determine whether it is a mirror


    def search(self, key):
        return self.search_A(self.root, key)

    def search_A(self, root, key):
        if root is None or root.val == key:
            return root is not None
        # if root is None:
           # return False
        # if root.val == key:
         #   return True
        if ((not self.mirrors and key < root.val) or (self.mirrors and key > root.val)):
            return self.search_A(root.left, key)
        return self.search_A(root.right, key)
        # Used for multiple judgment conditions
    def preorder(self):
        self.preorder_A(self.root)
        print()

    def preorder_A(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder_A(root.left)
            self.preorder_A(root.right)

    def remove(self, key):
        self.root = self.remove_A(self.root, key)
# Completely modify remove and add method
    def remove_A(self, root, key):
        if root is None:
            return root
        if ((not self.mirrors and key < root.val) or (self.mirrors and key > root.val)):
            root.left = self.remove_A(root.left, key)
        elif ((not self.mirrors and key > root.val) or (self.mirrors and key < root.val)):
            root.right = self.remove_A(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.find_min(root.left) if not self.mirrors else self.find_max(root.right)
            root.val = temp.val
            if not self.mirrors:
                root.left = self.remove_A(root.left, temp.val)
            else:
                root.right = self.remove_A(root.right, temp.val)
        return root
    def find_max(self, root):
        correct = root
        while correct.left is not None:
            correct = correct.left
        return correct

    def postorder(self):
        self.postorder_A(self.root)
        print()

    def postorder_A(self, node):
        if node is None:
            return
        self.postorder_A(node.left)
        self.postorder_A(node.right)
        print(node.val, end=' ')
# https://www.geeksforgeeks.org/binary-search-tree-traversal-inorder-preorder-post-order/?ref=lbp
    def inorder(self):
        self.inorder_A(self.root)
        print()

    def inorder_A(self, root):
        if root:
            self.inorder_A(root.left)
            print(root.val, end=' ')
            self.inorder_A(root.right)
# https://github.com/zyn10/breadthFirstSearch_python/blob/main/Source%20Codes/main.py
# I FIND THE CODE FROM GITHUB AND I JUST CHANGE STRUCTURE
    def breadthfirst(self):
        if self.root is None:
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.val, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def mirror(self):
        self.mirror_A(self.root)
        self.mirrors = not self.mirrors
    def mirror_A(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.mirror_A(root.left)
            self.mirror_A(root.right)
        return root



if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.mirror()
    Tree.preorder()         # 5 9 7 6 1 3 4 2

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))   # True
    Tree.preorder()         # 5 9 7 8 6 1 2 4
    Tree.mirror()
    Tree.preorder()         # 5 1 2 4 9 7 6 8

