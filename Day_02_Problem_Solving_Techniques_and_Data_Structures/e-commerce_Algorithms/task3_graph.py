from collections import deque

# ==========================================
# TASK 3: GRAPH - MICROSERVICE DEPENDENCIES
# ==========================================

class Graph:

    def __init__(self):
        self.graph = {}

    # Add service and dependencies
    def add_edge(self, service, dependency):
        if service not in self.graph:
            self.graph[service] = []

        if dependency not in self.graph:
            self.graph[dependency] = []

        self.graph[service].append(dependency)

    # BFS Traversal
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("BFS Traversal:")

        while queue:
            current = queue.popleft()

            if current not in visited:
                print(current, end=" ")
                visited.add(current)

                for neighbour in self.graph[current]:
                    if neighbour not in visited:
                        queue.append(neighbour)

    # DFS Traversal
    def dfs(self, start, visited=None):

        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=" ")
            visited.add(start)

            for neighbour in self.graph[start]:
                self.dfs(neighbour, visited)

    # Topological Sort
    def topological_sort(self):

        visited = set()
        stack = []

        def dfs_topological(node):

            if node not in visited:
                visited.add(node)

                for neighbour in self.graph[node]:
                    dfs_topological(neighbour)

                stack.append(node)

        for node in self.graph:
            if node not in visited:
                dfs_topological(node)

        return stack[::-1]

    # Cycle Detection
    def detect_cycle(self):

        visited = set()
        recursion_stack = set()

        def dfs_cycle(node):

            visited.add(node)
            recursion_stack.add(node)

            for neighbour in self.graph[node]:

                if neighbour not in visited:
                    if dfs_cycle(neighbour):
                        return True

                elif neighbour in recursion_stack:
                    return True

            recursion_stack.remove(node)
            return False

        for node in self.graph:

            if node not in visited:
                if dfs_cycle(node):
                    return True

        return False


# ==========================================
# MAIN PROGRAM
# ==========================================

g = Graph()

# Microservice dependencies
g.add_edge("Cart", "Pricing")
g.add_edge("Cart", "Inventory")

g.add_edge("Payment", "Authentication")

g.add_edge("Order", "Cart")
g.add_edge("Order", "Payment")

g.add_edge("Shipping", "Order")
g.add_edge("Notification", "Shipping")

print("=" * 50)
print("MICROSERVICE DEPENDENCY GRAPH")
print("=" * 50)

print("\nGraph Representation:")
for service, dependencies in g.graph.items():
    print(f"{service} -> {dependencies}")

print("\n")

# BFS
g.bfs("Order")

print("\n\nDFS Traversal:")
g.dfs("Order")

# Deployment order
print("\n\nDeployment Order:")
deployment_order = g.topological_sort()

for service in deployment_order:
    print(service, end=" -> ")

# Cycle detection
print("\n\nCycle Detection:")

if g.detect_cycle():
    print("Circular dependency detected!")
else:
    print("No circular dependency detected.")


# ==========================================
# CIRCULAR DEPENDENCY DEMONSTRATION
# ==========================================

print("\n" + "=" * 50)
print("CIRCULAR DEPENDENCY TEST")
print("=" * 50)

cycle_graph = Graph()

cycle_graph.add_edge("ServiceA", "ServiceB")
cycle_graph.add_edge("ServiceB", "ServiceC")
cycle_graph.add_edge("ServiceC", "ServiceA")

if cycle_graph.detect_cycle():
    print("Circular dependency detected!")
else:
    print("No circular dependency detected.")