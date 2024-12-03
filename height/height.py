class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


    def __str__(self):
        return str(self.value)

    def traverse_in_order(self):
        if self.left:
            self.left.traverse_in_order()

        print(self.data, end = " ")
        if self.right:
           self.right.traverse_in_order()

    def traverse_pre_order(self):
        print(self.data, end =" ")
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()

    def traverse_post_order(self):
        if self.left:
            self.left.traverse_post_order()
        if self.right:
            self.right.traverse_post_order()

        print(self.data, end = " ")

    def height(self, h=0):
        if self.left:
            leftheight = self.left.height(h+1)
        else:
            leftheight = h
        if self.right:
            rightheight = self.right.height(h+1)
        else:
            rightheight = h
        height = max(leftheight, rightheight)
        return height



class Tree:
    def __init__(self, root):
        self.root = Node(root)




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

    #      1
    #    /   \
    #   7      9
    #  / \       \
    # 2   6       9
    #    / \     /
    #   5  11   5


# Postorder Traverse
# 2 5 11 6 7 5 9 9 1
print(tree.root.height())