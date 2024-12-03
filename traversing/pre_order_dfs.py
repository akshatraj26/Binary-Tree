from collections import deque
class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


    def __str__(self):
        return str(self.data)





class Tree:
    def __init__(self, root):
        self.root = Node(root)


    def traverse_in_order(self, node):
        if node:
           self.traverse_in_order(node.left)
           print(node.data, end=" ")
           self.traverse_in_order(node.right)

    def traverse_pre_order(self, node):

        if node:
            print(node.data, end =" ")
            self.traverse_pre_order(node.left)
            self.traverse_pre_order(node.right)

    def traverse_post_order(self, node):
        if node:
            self.traverse_post_order(node.left)
            self.traverse_post_order(node.right)
            print(node.data, end = " ")

    def pre_order_iterative(self, node):
        stk = [node]

        while stk:
            node = stk.pop()
            if node.right: stk.append(node.right)
            if node.left: stk.append(node.left)
            print(node, end = " ")






tree = Tree(1)
tree.root.left = Node(7)
tree.root.right = Node(9)
tree.root.left.left = Node(2)
tree.root.left.right = Node(6)
tree.root.right.right = Node(9)
tree.root.right.right.left = Node(5)
tree.root.left.right.left = Node(5)
tree.root.left.right.right = Node(11)

# Tree Structure

    #     1
    #   7    9
    # 2   6     9
    #    5 11  5


# Postorder Traverse
# 2 5 11 6 7 5 9 9 1
tree.traverse_post_order(tree.root)
print("\n")
tree.pre_order_iterative(tree.root)