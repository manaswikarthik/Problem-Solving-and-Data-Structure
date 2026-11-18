# ============================================
# QUEUE IMPLEMENTATION
# Walk-in Patient Management (FIFO)
# ============================================

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)
        print(f"Added to queue: {patient}")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            patient = self.queue.pop(0)
            print(f"Patient served: {patient}")

    def display(self):
        print("Queue:", self.queue)


# ============================================
# STACK IMPLEMENTATION
# Recently Viewed Patients (LIFO)
# ============================================

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, patient):
        self.stack.append(patient)
        print(f"Patient viewed: {patient}")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            patient = self.stack.pop()
            print(f"Last viewed patient: {patient}")

    def display(self):
        print("Stack:", self.stack)


# ============================================
# MAIN PROGRAM
# ============================================

# Queue operations
print("\n========== QUEUE ==========")

q = Queue()

q.enqueue("Patient 101")
q.enqueue("Patient 102")
q.enqueue("Patient 103")

q.display()

q.dequeue()

q.display()


# Stack operations
print("\n========== STACK ==========")

s = Stack()

s.push("Patient 101")
s.push("Patient 102")
s.push("Patient 103")

s.display()

s.pop()

s.display()