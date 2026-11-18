# TASK 4: MANUAL REVIEW QUEUE AND ADJUSTMENT STACK

# ==================================================
# QUEUE IMPLEMENTATION
# ==================================================

class Queue:

    def __init__(self):
        self.items = []

    # Add transaction to queue
    def enqueue(self, transaction):
        self.items.append(transaction)

    # Remove transaction from front
    def dequeue(self):
        if len(self.items) == 0:
            return "Queue is empty"

        return self.items.pop(0)

    # Display queue
    def display(self):
        print("Queue:", self.items)


# ==================================================
# STACK IMPLEMENTATION
# ==================================================

class Stack:

    def __init__(self):
        self.items = []

    # Add adjustment to stack
    def push(self, adjustment):
        self.items.append(adjustment)

    # Remove latest adjustment
    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"

        return self.items.pop()

    # Display stack
    def display(self):
        print("Stack:", self.items)


# ==================================================
# QUEUE DEMONSTRATION
# ==================================================

print("=" * 50)
print("BANK TRANSACTION MANUAL REVIEW QUEUE")
print("=" * 50)

review_queue = Queue()

# Adding transactions
review_queue.enqueue("Transaction 101")
review_queue.enqueue("Transaction 102")
review_queue.enqueue("Transaction 103")

print("\nAfter adding transactions:")
review_queue.display()

# Processing transactions
print("\nProcessing transactions:")
print("Processed:", review_queue.dequeue())
print("Processed:", review_queue.dequeue())

print("\nRemaining transactions:")
review_queue.display()


# ==================================================
# STACK DEMONSTRATION
# ==================================================

print("\n" + "=" * 50)
print("BANK ADJUSTMENT UNDO STACK")
print("=" * 50)

adjustment_stack = Stack()

# Adding adjustments
adjustment_stack.push("Adjustment A")
adjustment_stack.push("Adjustment B")
adjustment_stack.push("Adjustment C")

print("\nAfter adding adjustments:")
adjustment_stack.display()

# Undoing adjustments
print("\nUndoing adjustments:")
print("Undo:", adjustment_stack.pop())
print("Undo:", adjustment_stack.pop())

print("\nRemaining adjustments:")
adjustment_stack.display()


# ==================================================
# COMPLEXITY ANALYSIS
# ==================================================

print("\n" + "=" * 50)
print("COMPLEXITY ANALYSIS")
print("=" * 50)

print("Queue Enqueue: O(1)")
print("Queue Dequeue: O(n)")
print("Stack Push: O(1)")
print("Stack Pop: O(1)")
print("Space Complexity: O(n)")