class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


    def __str__(self):
        return str(self.value)

    def traverse_in_order(self):
        if self.left:
            self.left.traverse_in_order()

        print(self.value, end = " ")
        if self.right:
            self.right.traverse_in_order()



class Tree:
    def __init__(self, root):
        self.root = Node(root)




tree = Node(1)
tree.left = Node(7)
tree.right = Node(9)
tree.left.left = Node(2)
tree.left.right = Node(6)
tree.right.right = Node(9)
tree.right.right.left = Node(5)
tree.left.right.left = Node(5)
tree.left.right.right = Node(11)

# Inorder Traverse
# 2 7 5 6 11 1 9 5 9
tree.traverse_in_order()