# Insurance Claims Management
# Task 1: Binary Search Tree (BST)


# Create a Node
class Node:
    def __init__(self, claim_id):
        self.claim_id = claim_id
        self.left = None
        self.right = None


# Create BST
class BST:

    def __init__(self):
        self.root = None

    # Insert a claim ID
    def insert(self, claim_id):

        if self.root is None:
            self.root = Node(claim_id)

        else:
            self._insert(self.root, claim_id)

    def _insert(self, node, claim_id):

        if claim_id < node.claim_id:

            if node.left is None:
                node.left = Node(claim_id)

            else:
                self._insert(node.left, claim_id)

        elif claim_id > node.claim_id:

            if node.right is None:
                node.right = Node(claim_id)

            else:
                self._insert(node.right, claim_id)

        # Ignore duplicate claim IDs


    # Search for a claim ID
    def search(self, claim_id):

        current = self.root

        while current is not None:

            if current.claim_id == claim_id:
                return True

            elif claim_id < current.claim_id:
                current = current.left

            else:
                current = current.right

        return False


    # Inorder Traversal: Left -> Root -> Right
    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)
            print(node.claim_id, end=" ")
            self.inorder(node.right)


    # Preorder Traversal: Root -> Left -> Right
    def preorder(self, node):

        if node is not None:
            print(node.claim_id, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


    # Postorder Traversal: Left -> Right -> Root
    def postorder(self, node):

        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.claim_id, end=" ")


# Main Program

bst = BST()

claim_ids = [
    105, 80, 120, 60, 90, 110, 140,
    50, 70, 85, 95, 108, 115, 130, 150
]

# Insert claim IDs
for claim_id in claim_ids:
    bst.insert(claim_id)


# Display Traversals
print("Inorder Traversal:")
bst.inorder(bst.root)

print("\n\nPreorder Traversal:")
bst.preorder(bst.root)

print("\n\nPostorder Traversal:")
bst.postorder(bst.root)


# Search Claims
print("\n\nClaim ID 110 exists:", bst.search(110))
print("Claim ID 999 exists:", bst.search(999))