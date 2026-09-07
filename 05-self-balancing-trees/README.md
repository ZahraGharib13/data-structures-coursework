# AVL Tree vs Splay Tree

This exercise compares two self-balancing search-tree approaches by building an **AVL tree** and a **Splay tree**, then measuring search costs for multiple query sequences.

## What It Demonstrates

- Binary search trees
- AVL trees
- Tree height and balance factors
- Left and right rotations
- AVL insertion and rebalancing
- Splay trees
- Zig, zig-zig, and zig-zag rotations
- Search-depth calculation
- Comparing search costs between tree structures

## How It Works

The program:

1. Reads the values used to build the trees.
2. Builds an AVL tree using recursive insertion and rotations.
3. Builds a Splay tree using parent pointers and splaying operations.
4. Processes several search sequences.
5. Computes the total AVL search depth for each sequence.
6. Computes the Splay-tree search cost while allowing the tree to restructure after successful searches.
7. Prints both costs for comparison.

## Run

```bash
python avl_vs_splay.py
```

## Input

The program expects:

1. the number of search sequences;
2. the values used to construct the trees;
3. one search sequence per following line.

## Project Structure

```text
05-self-balancing-trees/
├── avl_vs_splay.py
└── README.md
```

## About

This exercise was completed as part of a Data Structures course and demonstrates self-balancing search trees, rotations, adaptive restructuring, and search-cost comparison.
