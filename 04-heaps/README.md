# Heap Exercises

Exercises from the Data Structures course focused on heap behavior, deletion, and recursive reconstruction.

## Exercise 1 — Heap Deletion Candidates

`heap_deletion_candidates.py` checks which heap elements can be removed while still allowing the remaining structure to be restored as a valid complete min-heap.

### Concepts

- Array-based heap representation
- Complete binary tree indexing
- Parent/child relationships
- Recursive heap restoration
- Valid deletion candidates

## Exercise 2 — Count Possible Heap Deletion Orders

`heap_deletion_order_count.py` recursively explores valid deletion candidates and counts how many complete deletion orders are possible.

### Concepts

- Min-heap deletion
- Recursive search
- Backtracking-style enumeration
- Heap restructuring
- Counting valid operation sequences

### How It Works

The program:

1. Finds elements that can validly be deleted from the current heap.
2. Deletes one candidate and restores the heap.
3. Recursively repeats the process on the smaller heap.
4. Builds all valid deletion sequences.
5. Prints the number of possible sequences.

## Run

```bash
python heap_deletion_candidates.py
```

and:

```bash
python heap_deletion_order_count.py
```

## Project Structure

```text
04-heaps/
├── heap_deletion_candidates.py
├── heap_deletion_order_count.py
└── README.md
```

## About

These exercises were completed as part of a Data Structures course and demonstrate heap indexing, deletion logic, recursion, and enumeration of valid heap-operation sequences.
