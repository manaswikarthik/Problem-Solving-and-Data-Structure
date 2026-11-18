class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Insert a category
    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):

        if data < current.data:

            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)

        else:

            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    # Search for a category
    def search(self, data):

        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):

        if current is None:
            return False

        if current.data == data:
            return True

        elif data < current.data:
            return self._search_recursive(current.left, data)

        else:
            return self._search_recursive(current.right, data)

    # Inorder Traversal: Left -> Root -> Right
    def inorder(self, current):

        if current:
            self.inorder(current.left)
            print(current.data, end=" ")
            self.inorder(current.right)

    # Preorder Traversal: Root -> Left -> Right
    def preorder(self, current):

        if current:
            print(current.data, end=" ")
            self.preorder(current.left)
            self.preorder(current.right)

    # Postorder Traversal: Left -> Right -> Root
    def postorder(self, current):

        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data, end=" ")



bst = BinarySearchTree()

# 15 Product Categories
categories = [
    "Electronics",
    "Books",
    "Clothing",
    "Furniture",
    "Groceries",
    "Mobiles",
    "Laptops",
    "Shoes",
    "Accessories",
    "Beauty",
    "Sports",
    "Toys",
    "HomeDecor",
    "Watches",
    "Stationery"
]

# Insert categories
for category in categories:
    bst.insert(category)

print("=" * 50)
print("E-COMMERCE PRODUCT CATEGORY BST")
print("=" * 50)

print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\n\nPreorder Traversal:")
bst.preorder(bst.root)

print("\n\nPostorder Traversal:")
bst.postorder(bst.root)

# Search operation
search_category = "Laptops"

print("\n\nSearch Result:")

if bst.search(search_category):
    print(f"{search_category} category found.")
else:
    print(f"{search_category} category not found.")

# Search for a missing category
search_category = "Gaming"

if bst.search(search_category):
    print(f"{search_category} category found.")
else:
    print(f"{search_category} category not found.")