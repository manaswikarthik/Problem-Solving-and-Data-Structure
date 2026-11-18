# Logistics Network and Delivery Windows
# Task 3: Graph using BFS and DFS

from collections import deque

# -----------------------------------
# Logistics Network - 10 Hubs
# -----------------------------------

graph = {
    "CHN": ["BLR", "HYD"],
    "BLR": ["CHN", "MYS", "CBE"],
    "HYD": ["CHN", "VJA", "BOM"],
    "MYS": ["BLR"],
    "CBE": ["BLR", "KOC"],
    "VJA": ["HYD", "DEL"],
    "BOM": ["HYD", "PUN", "DEL"],
    "KOC": ["CBE"],
    "DEL": ["VJA", "BOM"],
    "PUN": ["BOM"]
}


# -----------------------------------
# BFS - Shortest Route
# -----------------------------------

def bfs_shortest_route(graph, start, destination):

    queue = deque([(start, [start])])
    visited = set()

    while queue:

        current, path = queue.popleft()

        if current == destination:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None


# -----------------------------------
# DFS - Reachable Hubs
# -----------------------------------

def dfs_reachable(graph, start):

    visited = set()

    def dfs(node):

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)

    return visited


# -----------------------------------
# Main Program
# -----------------------------------

print("=" * 60)
print("LOGISTICS NETWORK MANAGEMENT")
print("TASK 3: GRAPH - BFS & DFS")
print("=" * 60)


# Display adjacency list
print("\nLOGISTICS NETWORK - ADJACENCY LIST")
print("-" * 60)

for hub, routes in graph.items():
    print(f"{hub} -> {routes}")


# -----------------------------------
# BFS Shortest Route
# -----------------------------------

print("\n" + "-" * 60)
print("SHORTEST ROUTE USING BFS")
print("-" * 60)

start = "CHN"
destination = "DEL"

route = bfs_shortest_route(graph, start, destination)

if route:
    print(f"Starting Hub: {start}")
    print(f"Destination Hub: {destination}")
    print("Shortest Route:", " -> ".join(route))
    print("Number of Hops:", len(route) - 1)
else:
    print("No route available.")


# -----------------------------------
# DFS Reachable Hubs
# -----------------------------------

print("\n" + "-" * 60)
print("REACHABLE HUBS USING DFS")
print("-" * 60)

central_depot = "CHN"

reachable = dfs_reachable(graph, central_depot)

print(f"Central Depot: {central_depot}")
print("Reachable Hubs:")

for hub in sorted(reachable):
    print(hub)

print("Total Reachable Hubs:", len(reachable))


# -----------------------------------
# Test Case
# -----------------------------------

print("\n" + "-" * 60)
print("TEST CASE")
print("-" * 60)

test_start = "MYS"
test_destination = "KOC"

test_route = bfs_shortest_route(
    graph,
    test_start,
    test_destination
)

if test_route:
    print(f"Route from {test_start} to {test_destination}:")
    print(" -> ".join(test_route))
else:
    print("No route found.")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED")
print("=" * 60)