# E-Commerce Platform – Data Structures & Algorithms

## Business Scenario
An e-commerce platform requires efficient category browsing, fast SKU look-ups, dependency management for microservices, traffic analysis, and order-value matching.

## Tasks

### Task 1 – Product Category Management
- Build a Binary Search Tree (BST) using 15 sample product categories.
- Implement insertion and searching.
- Display Inorder, Preorder, and Postorder traversals.

### Task 2 – SKU Lookup
- Implement a hash table using chaining.
- Demonstrate a hash collision.
- Compare lookup performance between the custom hash table and Python's built-in dictionary using 100,000 SKUs.

### Task 3 – Microservice Deployment
- Model microservice dependencies using a graph.
- Implement BFS and DFS to determine deployment order.
- Detect circular dependencies.

### Task 4 – Peak Traffic Analysis
- Use requests-per-minute data for 24 hours.
- Apply the sliding window technique to find the busiest continuous 3-hour window.

### Task 5 – Gift Card Matching
- Given a sorted list of order values, use the two-pointer technique.
- Find all pairs whose sum equals the gift-card value.

## Deliverables
- Python source code for all five tasks.
- Execution output demonstrating each task.
- Decision table explaining the problem, algorithm/data structure used, and its purpose.

## Decision Table

| Task | Problem | Data Structure / Algorithm | Reason |
|---|---|---|---|
| 1 | Category insertion and search | Binary Search Tree (BST) | Efficient searching and maintaining sorted category data |
| 2 | SKU lookup | Hash Table with Chaining / Dictionary | Fast key-based lookup and collision handling |
| 3 | Service deployment | Graph, BFS, DFS, Cycle Detection | Manage dependencies and determine deployment order |
| 4 | Peak traffic | Sliding Window | Efficiently find the busiest continuous time period |
| 5 | Gift-card matching | Two Pointers | Find matching pairs in a sorted list efficiently |

## Technologies Used
- Python 3
- Data Structures
- Algorithms

## Project Structure

```text
E-Commerce-Algorithms/
│
├── task1_bst.py
├── task2_hash_table.py
├── task3_graph.py
├── task4_sliding_window.py
├── task5_two_pointers.py
├── README.md
└── output/
    └── execution_output.txt
```

## Conclusion
This case study demonstrates how fundamental data structures and algorithms can solve practical e-commerce problems, improving lookup efficiency, deployment planning, traffic analysis, and order processing.