# Binary Tree and Binary Search Tree (BST) Implementation

This repository contains an implementation of a **Binary Tree** and **Binary Search Tree (BST)** with traversal and search functionalities. It is designed to provide a clear understanding of tree data structures and their operations.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Binary Tree Operations](#binary-tree-operations)
3. [Binary Search Tree (BST) Operations](#binary-search-tree-bst-operations)
4. [Traversals](#traversals)
5. [Searching](#searching)
6. [Getting Started](#getting-started)
7. [Code Examples](#code-examples)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction

A **Binary Tree** is a hierarchical data structure where each node has at most two children, referred to as the **left child** and **right child**. A **Binary Search Tree (BST)** is a special type of binary tree where the left subtree of a node contains only nodes with values less than the node’s value, and the right subtree contains only nodes with values greater than the node’s value.

### Key Features:
- **Binary Tree** for general-purpose hierarchical data organization.
- **Binary Search Tree (BST)** for efficient searching, insertion, and deletion.
- Support for common **tree traversal methods**: In-order, Pre-order, Post-order, and Level-order.
- Searching algorithms for locating specific nodes.

---

## Binary Tree Operations

### 1. **Insertion**
Nodes can be added to a binary tree at the first available position in a level-order manner.

### 2. **Traversal**
Binary Trees support traversal methods to visit all nodes in a specific order:
- In-order Traversal
- Pre-order Traversal
- Post-order Traversal
- Level-order Traversal

---

## Binary Search Tree (BST) Operations

### 1. **Insertion**
Values are inserted into the BST while maintaining the BST property:
- Values smaller than the current node are placed in the left subtree.
- Values larger than the current node are placed in the right subtree.

### 2. **Deletion**
Nodes can be removed from the BST while ensuring the BST property remains intact.

### 3. **Searching**
Locate a node based on its value using the properties of the BST.

---

## Traversals

### 1. **In-order Traversal (Left, Root, Right)**
Yields nodes in ascending order for BSTs.

### 2. **Pre-order Traversal (Root, Left, Right)**
Useful for creating a copy of the tree.

### 3. **Post-order Traversal (Left, Right, Root)**
Useful for deleting or freeing nodes.

### 4. **Level-order Traversal**
Visits nodes level by level, from top to bottom.

---

## Searching

### Binary Tree Search
Searches each node until the desired value is found (or the tree is exhausted).
- **Time Complexity:** O(n)

### Binary Search Tree Search
Searches the tree using the BST property, reducing the search space at each step.
- **Time Complexity:** O(log n) (average case)

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/username/binary-tree-bst.git
cd binary-tree-bst
```

---

## Code Examples

### Creating and Traversing a Binary Search Tree
```python
from binary_tree import BinarySearchTree

# Create a new BST
bst = BinarySearchTree()

# Insert elements
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Traversals
print("In-order Traversal:", bst.in_order_traversal())
print("Pre-order Traversal:", bst.pre_order_traversal())
print("Post-order Traversal:", bst.post_order_traversal())
```

### Searching in a BST
```python
# Search for a value
found = bst.search(40)
print("Found 40:", found)
```

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out for questions or collaborations!