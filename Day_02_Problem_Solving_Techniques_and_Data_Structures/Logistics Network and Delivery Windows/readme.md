# Logistics Network and Delivery Windows

## Business Scenario

A courier company optimizes hub-to-hub routing, parcel tracking, delivery planning, and route validation across a logistics network.

## Tasks Implemented

### Task 1 – Binary Search Tree (BST)
- Insert and search hub codes.
- Calculate BST height.
- Demonstrate the effect of sorted input on tree height.

### Task 2 – Hash Map
- Store parcel tracking numbers.
- Track parcel scans at different hubs.
- Detect duplicate scans at the same hub.

### Task 3 – Graphs
- Represent 10 logistics hubs using an adjacency list.
- Find the shortest route using BFS.
- Identify reachable hubs using DFS.

### Task 4 – Sliding Window
- Find the 4-hour window with the highest average parcel count.

### Task 5 – Two Pointers
- Check whether a route of hub codes is a palindrome.
- Ignore case differences and separators.

## Project Structure

```text
Logistics-Network-Algorithms/
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

```bash
python task1_bst.py
python task2_hashing.py
python task3_graph.py
python task4_sliding_window.py
python task5_two_pointers.py
```

## Graph Adjacency List

```text
CHN -> BLR, HYD
BLR -> CHN, MYS, CBE
HYD -> CHN, VJA, BOM
MYS -> BLR
CBE -> BLR, KOC
VJA -> HYD, DEL
BOM -> HYD, PUN, DEL
KOC -> CBE
DEL -> VJA, BOM
PUN -> BOM
```

## Complexity Analysis

| Task | Algorithm | Time Complexity | Space Complexity |
|------|-----------|----------------|-----------------|
| 1 | BST Insert/Search | Average O(log n), Worst O(n) | O(n) |
| 2 | Hash Map | Average O(1) lookup | O(n × k) |
| 3 | BFS / DFS | O(V + E) | O(V) |
| 4 | Sliding Window | O(n) | O(k) |
| 5 | Two Pointers | O(n) | O(n) |

## Testing

Each program includes test cases covering normal inputs and relevant edge cases.

## Conclusion

This project demonstrates the practical application of data structures and algorithms for logistics routing, parcel tracking, delivery optimization, and route validation.