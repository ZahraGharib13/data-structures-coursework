# Heap Exercises

Exercises from the Data Structures course focused on heap behavior and deletion.

## Exercise 1 — Heap Deletion Candidates

`heap_deletion_candidates.py` determines which elements of a heap can be removed while still allowing the remaining structure to be restored as a valid complete min-heap.

## What It Demonstrates

- Array-based heap representation
- Complete binary tree indexing
- Parent/child relationships
- Recursive heap restoration
- Candidate checking after deletion

## How It Works

For each possible deletion candidate, the program:

1. Copies the heap.
2. Removes the selected element.
3. Replaces the gap by repeatedly moving the smaller child upward.
4. Recursively checks whether the deletion can end at the final array position.
5. Prints all values that can be valid deletion candidates.

## Run

```bash
python heap_deletion_candidates.py
```

## Project Structure

```text
04-heaps/
├── heap_deletion_candidates.py
└── README.md
```

A second heap exercise will be added to this same folder.
