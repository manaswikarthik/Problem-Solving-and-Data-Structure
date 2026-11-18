from collections import deque
import time

# ==========================================
# 1. CUSTOM STACK IMPLEMENTATION
# ==========================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


# ==========================================
# 2. CUSTOM QUEUE IMPLEMENTATION
# ==========================================

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


# ==========================================
# 3. STACK - UNDO ORDER EDIT
# ==========================================

print("=" * 60)
print("              STACK - UNDO ORDER EDIT")
print("=" * 60)

custom_stack = Stack()

# Store order edits
custom_stack.push("Order 101: Amount changed to 500")
custom_stack.push("Order 102: Address changed")
custom_stack.push("Order 103: Quantity changed")

print("\nOrder edits:")
custom_stack.display()

print("\nUndoing last edit:")
print(custom_stack.pop())

print("\nRemaining edits:")
custom_stack.display()


# ==========================================
# 4. BUILT-IN STACK COMPARISON
# ==========================================

builtin_stack = []

builtin_stack.append("Order 101: Amount changed to 500")
builtin_stack.append("Order 102: Address changed")
builtin_stack.append("Order 103: Quantity changed")

print("\nBuilt-in Stack:")
print(builtin_stack)

print("\nUndoing last edit:")
print(builtin_stack.pop())

print("Remaining edits:")
print(builtin_stack)


# ==========================================
# 5. QUEUE - DISPATCH ORDERS
# ==========================================

print("\n" + "=" * 60)
print("              QUEUE - DISPATCH LINE")
print("=" * 60)

custom_queue = Queue()

custom_queue.enqueue("Order 101")
custom_queue.enqueue("Order 102")
custom_queue.enqueue("Order 103")

print("\nDispatch line:")
custom_queue.display()

print("\nDispatching order:")
print(custom_queue.dequeue())

print("\nRemaining orders:")
custom_queue.display()


# ==========================================
# 6. BUILT-IN QUEUE COMPARISON
# ==========================================

builtin_queue = deque()

builtin_queue.append("Order 101")
builtin_queue.append("Order 102")
builtin_queue.append("Order 103")

print("\nBuilt-in Queue:")
print(list(builtin_queue))

print("\nDispatching order:")
print(builtin_queue.popleft())

print("Remaining orders:")
print(list(builtin_queue))


# ==========================================
# 7. PERFORMANCE COMPARISON
# ==========================================

print("\n" + "=" * 60)
print("              PERFORMANCE COMPARISON")
print("=" * 60)

# Stack performance
custom_stack = Stack()
builtin_stack = []

iterations = 100000

start = time.perf_counter()

for i in range(iterations):
    custom_stack.push(i)

for i in range(iterations):
    custom_stack.pop()

custom_stack_time = time.perf_counter() - start


start = time.perf_counter()

for i in range(iterations):
    builtin_stack.append(i)

for i in range(iterations):
    builtin_stack.pop()

builtin_stack_time = time.perf_counter() - start


# Queue performance
custom_queue = Queue()
builtin_queue = deque()

start = time.perf_counter()

for i in range(iterations):
    custom_queue.enqueue(i)

for i in range(iterations):
    custom_queue.dequeue()

custom_queue_time = time.perf_counter() - start


start = time.perf_counter()

for i in range(iterations):
    builtin_queue.append(i)

for i in range(iterations):
    builtin_queue.popleft()

builtin_queue_time = time.perf_counter() - start


print(f"\nCustom Stack Time: {custom_stack_time:.6f} seconds")
print(f"Built-in Stack Time: {builtin_stack_time:.6f} seconds")

print(f"\nCustom Queue Time: {custom_queue_time:.6f} seconds")
print(f"Built-in Queue Time: {builtin_queue_time:.6f} seconds")

print("=" * 60)