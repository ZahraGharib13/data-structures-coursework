# Binary Tree Inorder Traversal

This exercise reconstructs a binary tree from parent-child relationships and prints its **inorder traversal**.

## What It Demonstrates

- Binary tree representation
- Parent/child relationships
- Root detection
- Recursive tree traversal
- Inorder traversal: Left → Root → Right

## Input Format

The program first reads the number of nodes.

Then it reads `n - 1` relationships in the form:

```text
parent child direction
```

where `direction` is either:

```text
left
```

or:

```text
right
```

## How It Works

The program:

1. Stores left/right child relationships in a dictionary.
2. Tracks which nodes appear as children.
3. Finds the root by locating the node that never appears as a child.
4. Traverses the tree recursively in inorder.
5. Prints the traversal sequence.

## Run

```bash
python inorder_traversal.py
```

## Complexity

For a tree with `n` nodes:

- Building the relationships: `O(n)`
- Inorder traversal: `O(n)`
- Extra space: `O(n)`

## Project Structure

```text
03-binary-trees/
├── inorder_traversal.py
└── README.md
```

## About

This exercise was completed as part of a Data Structures course and demonstrates binary-tree construction and recursive traversal.
