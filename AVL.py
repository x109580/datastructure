class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.balance = 0
        self.height = 1

class AVL:
    def __init__(self) -> None:
        self.root = None
        self.is_balanced = True

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.right) - self.height(node.left)

    def right_rotation(self, root): #according to the VAL Tree
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))

        root.balance = self.balance(root)
        new_root.balance = self.balance(new_root)

        return new_root

    def left_rotation(self, root): #according to the VAL Tree
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))

        root.balance = self.balance(root)
        new_root.balance = self.balance(new_root)

        return new_root

    def right_left_rotation(self, root: AVLNode):
        root.right = self.right_rotation(root.right)
        return self.left_rotation(root)

    def left_right_rotation(self, root: AVLNode):
        root.left = self.left_rotation(root.left)
        return self.right_rotation(root)

    def insert(self, key):
        self.root = self.insert_help(self.root, key)

    def insert_help(self, root, key):
        if not root:
            root = AVLNode(key)
            self.is_balanced = False

        if key < root.key:
            root.left = self.insert_help(root.left, key)
            root.balance = self.balance(root)
        elif key > root.key:
            root.right = self.insert_help(root.right, key)
            root.balance = self.balance(root)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        root.balance = self.balance(root)
        if root.balance > 1:
            if self.balance(root.right) < 0:
                return self.right_left_rotation(root)
            else:
                return self.left_rotation(root)
        if root.balance < -1:
            if self.balance(root.left) > 0:
                return self.left_right_rotation(root)
            else:
                return self.right_rotation(root)

        return root

    def preorder(self):
        self.preorder_helper(self.root)

    def preorder_helper(self, root):
        if root:
            print(f"{root.key};{root.balance}", end=" ")
            self.preorder_helper(root.left)
            self.preorder_helper(root.right)


if __name__ == "__main__":
    Tree = AVL()
    for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
        Tree.insert(key)
    Tree.preorder()