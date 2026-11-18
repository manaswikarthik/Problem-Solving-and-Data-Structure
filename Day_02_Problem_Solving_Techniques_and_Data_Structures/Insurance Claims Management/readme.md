# Insurance Claims Management – Algorithms

## Business Scenario
An insurance company needs efficient algorithms to manage claim records, identify duplicate claims, track approval workflows, monitor claim spikes, and merge regional claim data.

## Tasks Implemented

### Task 1 – Binary Search Tree (BST)
- Insert and search claim IDs.
- Implement inorder, preorder, and postorder traversals.
- Inorder traversal displays claim IDs in sorted order.

### Task 2 – Hashing
- Detect duplicate claims using policy number and incident date.
- Normalize policy numbers to handle case and spacing differences.
- Use a Python set for efficient duplicate detection.

### Task 3 – Graphs
- Represent the claim approval workflow using a directed graph.
- Use BFS to find the shortest approval path.
- Use DFS to detect cycles in the workflow.

### Task 4 – Sliding Window / Consecutive Run
- Identify the longest consecutive period during which daily claims exceeded 100.
- Determine the starting and ending days of the maximum run.

### Task 5 – Two Pointers
- Merge two sorted regional claim lists.
- Maintain sorted order without using sorting functions.

## Project Structure

```text
Insurance-Claims-Algorithms/
├── task1_bst.py
├── task2_hashing.py
├── task3_graph.py
├── task4_sliding_window.py
├── task5_two_pointers.py
└── README.md
```

## Technologies Used
- Python
- Data Structures
- Algorithms

## Execution

Run individual programs using:

```bash
python task1_bst.py
python task2_hashing.py
python task3_graph.py
python task4_sliding_window.py
python task5_two_pointers.py
```

## Complexity Analysis

| Task | Algorithm | Time Complexity | Space Complexity |
|---|---|---|---|
| 1 | BST Insert/Search | Average O(log n), Worst O(n) | O(n) |
| 2 | Hashing | Average O(1) per operation | O(n) |
| 3 | BFS / DFS | O(V + E) | O(V) |
| 4 | Consecutive Run | O(n) | O(1) |
| 5 | Two Pointers | O(n + m) | O(n + m) |

## Testing
Each program includes test cases covering normal inputs, empty inputs, duplicates, and relevant edge cases.

## Conclusion
This project demonstrates the practical application of fundamental data structures and algorithms in an insurance claims management system.