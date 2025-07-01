class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def remove_rear(self):
        if self.is_empty():
            return None
        data = self.rear.data
        if self.front == self.rear:
            # Only one element in the deque
            self.front = self.rear = None
        else:
            current = self.front
            while current.next != self.rear:
                current = current.next
            self.rear = current
            self.rear.next = None
        return data




