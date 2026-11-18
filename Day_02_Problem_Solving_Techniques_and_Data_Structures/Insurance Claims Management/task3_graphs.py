# Insurance Claims Management
# Task 3: Claim Approval Workflow using Graphs
# BFS - Shortest Path
# DFS - Cycle Detection


from collections import deque


# ------------------------------------------
# 1. GRAPH REPRESENTATION
# ------------------------------------------

graph = {
    "Registration": ["Assessment"],
    "Assessment": ["Surveyor"],
    "Surveyor": ["Settlement"],
    "Settlement": []
}


# ------------------------------------------
# 2. BFS - SHORTEST PATH
# ------------------------------------------

def bfs_shortest_path(graph, start, destination):

    queue = deque()
    queue.append((start, [start]))

    visited = set()

    while queue:

        current, path = queue.popleft()

        if current == destination:
            return path

        if current not in visited:

            visited.add(current)

            for neighbor in graph.get(current, []):
                queue.append((neighbor, path + [neighbor]))

    return None


# ------------------------------------------
# 3. DFS - CYCLE DETECTION
# ------------------------------------------

def detect_cycle(graph):

    visited = set()
    recursion_stack = set()

    def dfs(node):

        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph.get(node, []):

            if neighbor not in visited:

                if dfs(neighbor):
                    return True

            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)

        return False

    for node in graph:

        if node not in visited:

            if dfs(node):
                return True

    return False


# ------------------------------------------
# 4. MAIN PROGRAM
# ------------------------------------------

print("=" * 50)
print("INSURANCE CLAIM APPROVAL WORKFLOW")
print("=" * 50)


# Display the graph
print("\nClaim Approval Stages:")

for stage, next_stages in graph.items():
    print(f"{stage} -> {next_stages}")


# Find shortest path using BFS
print("\n" + "-" * 50)

start = "Registration"
destination = "Settlement"

path = bfs_shortest_path(graph, start, destination)

print("Shortest Path using BFS:")

if path:
    print(" -> ".join(path))
else:
    print("No path found")


# Detect cycle using DFS
print("\n" + "-" * 50)

print("Cycle Detection using DFS:")
print("Cycle Detected:", detect_cycle(graph))


# Add a circular dependency
print("\n" + "-" * 50)

print("Adding Circular Dependency...")
graph["Settlement"].append("Registration")


# Check cycle again
print("Updated Workflow:")

for stage, next_stages in graph.items():
    print(f"{stage} -> {next_stages}")

print("\nCycle Detected:", detect_cycle(graph))


print("\n" + "=" * 50)
print("PROGRAM COMPLETED")
print("=" * 50)