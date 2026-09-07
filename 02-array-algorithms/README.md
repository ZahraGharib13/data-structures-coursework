# Maximum Profit — Linear Scan

This exercise finds the maximum possible profit from a sequence of prices using a single left-to-right scan.

## What It Demonstrates

- Array/list traversal
- Tracking a running minimum
- Greedy-style reasoning
- Linear-time processing

## How It Works

The algorithm keeps track of the minimum price seen so far.

For each next price, it computes:

```text
current profit = current price - minimum price seen so far
```

It then updates the best profit found.

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Run

```bash
python max_profit.py
```

Example input:

```text
7 1 5 3 6 4
```

## Project Structure

```text
02-array-algorithms/
├── max_profit.py
└── README.md
```

## About

This exercise was completed as part of a Data Structures course and demonstrates efficient one-pass array processing.
