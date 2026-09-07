# Shortest Prefix Cover

This exercise uses dynamic programming to find the **smallest prefix length** whose occurrences can cover the entire input text.

## What It Demonstrates

- Prefix checking
- Dynamic programming
- String processing
- Overlapping occurrences
- Searching for a minimum valid prefix length

## How It Works

For every possible prefix length `k`:

1. The candidate prefix is defined as `text[:k]`.
2. A DP array tracks which positions of the text have been covered.
3. Whenever the prefix matches starting at a currently reachable position, the newly covered positions are marked.
4. The first prefix length that can cover the entire text is printed.

Because covered positions can become starting points for later matches, the algorithm allows **overlapping occurrences** of the prefix.

## Important Input Note

The original coursework reads space-separated integers and concatenates them into one string:

```python
string = list(map(int, input().split()))
text = ''.join(str(num) for num in string)
```

For example:

```text
1 2 1 2
```

becomes:

```text
1212
```

If the intended input consists of single digits, this is fine.

If multi-digit integers are intended to remain separate elements, the representation should be changed because inputs such as `12 3` and `1 23` both become `123`.

## Run

```bash
python shortest_prefix_cover.py
```

## Complexity

The current implementation tries every prefix length and scans the text using a DP array. Its straightforward nested loops favor clarity over optimal asymptotic performance.

## Project Structure

```text
06-dynamic-programming/
├── shortest_prefix_cover.py
└── README.md
```

## About

This exercise was completed as part of a Data Structures course and demonstrates dynamic programming applied to prefix-based string covering.
