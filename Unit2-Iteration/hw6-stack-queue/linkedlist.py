'''
Mr. Chung
3/8: Linked List
'''

from node import Node

class LinkedList:
    # Constructor: set default attributes
    def __init__(self):
        self.head = None
        self.length = 0

    # Add new node to the end of the list
    def append(self, val):
        # Create a new Node with val as the value
        new_node = Node(val)
        # If the list is currently empty
        if self.head == None:
            self.head = new_node
        # Otherwise, find the end of the list
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            # curr is now pointing to the last node, so we set its `next` to the new node
            curr.next = new_node
        self.length += 1

    # Add new node to the front of the list
    def add_front(self, val):
        # 1) Create new node
        new_node = Node(val)
        # 2) Point new node's `next` to the old self.head
        new_node.next = self.head
        # 3) Make self.head point to new node
        self.head = new_node

        self.length += 1

    # Remove and return first value in list
    def pop(self):
        if self.head == None:
            return None
        first_val = self.head.val
        self.head = self.head.next
        self.length -= 1
        return first_val

    # Get the value at index i
    def get(self, i):
        # Make sure the requested index is valid
        if i < 0 or i >= self.length:
            return None
        # Begin curr at self.head (aka index 0)
        curr = self.head
        # Move curr i times to get to index i
        for x in range(i):
            curr = curr.next
        return curr.val

    # Empty the list
    def clear(self):
        self.head = None
        self.length = 0

    # Check if the list is empty
    def is_empty(self):
        return self.head == None

    # Print out every value in the list
    def print(self):
        print('=' * 20)
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next

    # Get the number of nodes in the list
    def size(self):
        return self.length
        # curr = self.head
        # count = 0
        # while curr != None:
        #     count += 1
        #     curr = curr.next
        # return count
