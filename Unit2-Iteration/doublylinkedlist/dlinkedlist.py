from dnode import Node

class DLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # Prints the contents of the list
    def print(self):
        result = '{'
        curr = self.head
        while curr is not None:
            result += str(curr.data)
            if curr.next is not None:
                result += ', '
            curr = curr.next
        result += '}'
        print(result)

    # Adds new node to the front of the list
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    # Adds new node to the end of the list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        self.length += 1

    # Inserts new node at the specified position
    def insert(self, new_data, pos):
        if pos < 0 or pos > self.length:
            print('Index out of range.')
        elif pos == 0:
            self.push(new_data)
        elif pos == self.length:
            self.append(new_data)
        else:
            count = 0
            curr = self.head
            while count < pos:
                curr = curr.next
                count += 1
            new_node = Node(new_data)
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev.next = new_node
            curr.prev = new_node
            self.length += 1

    # Deletes the first occurrence of the given value
    def delete(self, val):
        if self.head is None:
            print('Value not found.')
            return
        # Special case: target is head, need to update head
        if self.head.data == val:
            self.head = self.head.next
            self.head.prev = None
            return
        curr = self.head
        # Loop through all nodes
        while curr is not None:
            # Break the loop if we find the target
            if curr.data == val:
                break
            curr = curr.next
        # If loop ended naturally, then we didn't find the target
        if curr is None:
            print('Value not found.')
            return
        # Skip the target L->R
        curr.prev.next = curr.next
        # Skip the target R->L; be careful about hitting the end
        if curr.next is not None:
            curr.next.prev = curr.prev

    # Returns the index of the first occurrence of val (-1 if not found)
    def index(self, val):
        count = 0
        curr = self.head
        while curr is not None:
            if curr.data == val:
                return count
            curr = curr.next
            count += 1
        return -1

    # Returns the length of the list
    def size(self):
        return self.length
