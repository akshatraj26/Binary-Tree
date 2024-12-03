class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


    def __str__(self):
        return str(self.data)

    def in_order_traversing(self):
        if self.left:
            self.left.in_order_traversing()
        print(self.data, end=" ",)
        if self.right:
            self.right.in_order_traversing()

    def pre_order_traversing(self):
        print(self.data, end =" ")
        if self.left:
            self.left.pre_order_traversing()
        if self.right:
            self.right.pre_order_traversing()

    def post_order_traversing(self):
        if self.left:
            self.left.post_order_traversing()
        if self.right: self.right.post_order_traversing()
        print(self.data, end=" ")

    def height(self, h = 0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightheight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightheight)

    def search(self, target):

        if self.data == target:
            # print("Found it")
            return self

        if self.left and target < self.data :
            return self.left.search(target)
        if self.right and target > self.data: return self.right.search(target )







class BinaryTree:
    def __init__(self, root, name=None):
        self.root = Node(root)
        self.name = name


tree = BinaryTree(8, name="Binary Search Tree")
tree.root.left = Node(3)
tree.root.right = Node(10)
tree.root.left.left = Node(1)
tree.root.left.right = Node(6)
tree.root.left.right.left = Node(4)
tree.root.left.right.right = Node(7)
tree.root.right.right = Node(14)
tree.root.right.right.left = Node(13)

# 1 3 4 6 7 8 10 13 14
print("In Order Traversing")
tree.root.in_order_traversing()
print("\n")
# 8 3 1 6 4 7 10 14 13
print("Pre Order Traversing")
tree.root.pre_order_traversing()
print("\n")
# 1 4 7 6 3 13 14 10 8
print("Post Order Traversing")
tree.root.post_order_traversing()

print("\n")
print("Height of the tree:- ", tree.root.height())


print("\n")
found = tree.root.search(target=4)
print(found)