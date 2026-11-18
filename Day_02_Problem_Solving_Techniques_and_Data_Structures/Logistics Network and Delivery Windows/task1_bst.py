# Logistics Network and Delivery Windows
# Task 1: Binary Search Tree for Hub Codes

class Node:
    def __init__(self, hub_code):
        self.hub_code = hub_code
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # Insert a hub code
    def insert(self, hub_code):
        if self.root is None:
            self.root = Node(hub_code)
        else:
            self._insert(self.root, hub_code)

    def _insert(self, node, hub_code):
        if hub_code < node.hub_code:
            if node.left is None:
                node.left = Node(hub_code)
            else:
                self._insert(node.left, hub_code)

        elif hub_code > node.hub_code:
            if node.right is None:
                node.right = Node(hub_code)
            else:
                self._insert(node.right, hub_code)

    # Search for a hub code
    def search(self, hub_code):
        current = self.root

        while current is not None:
            if current.hub_code == hub_code:
                return True

            elif hub_code < current.hub_code:
                current = current.left

            else:
                current = current.right

        return False

    # Calculate tree height
    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    # Inorder traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.hub_code, end=" ")
            self.inorder(node.right)


# -----------------------------------
# Main Program
# -----------------------------------

print("=" * 50)
print("LOGISTICS NETWORK MANAGEMENT")
print("TASK 1: BINARY SEARCH TREE")
print("=" * 50)

# Hub codes
hub_codes = [50, 30, 70, 20, 40, 60, 80]

bst = BST()

print("\nInserting Hub Codes:")
for code in hub_codes:
    bst.insert(code)
    print(code, end=" ")

print("\n\nBST Inorder Traversal:")
bst.inorder(bst.root)

print("\n\nTree Height:")
print(bst.height(bst.root))

# Search
print("\n" + "-" * 50)
print("HUB SEARCH")

search_code = 60

if bst.search(search_code):
    print(f"Hub {search_code} found.")
else:
    print(f"Hub {search_code} not found.")

search_code = 100

if bst.search(search_code):
    print(f"Hub {search_code} found.")
else:
    print(f"Hub {search_code} not found.")

# -----------------------------------
# Sorted Input Demonstration
# -----------------------------------

print("\n" + "-" * 50)
print("SORTED INPUT DEMONSTRATION")

sorted_codes = [10, 20, 30, 40, 50, 60, 70]

sorted_bst = BST()

for code in sorted_codes:
    sorted_bst.insert(code)

print("Sorted Hub Codes:")
sorted_bst.inorder(sorted_bst.root)

print("\nHeight of BST with Sorted Input:")
print(sorted_bst.height(sorted_bst.root))

print("\n" + "=" * 50)
print("PROGRAM COMPLETED")
print("=" * 50)