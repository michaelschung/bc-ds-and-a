from node import Node

class LinkedList:
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
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # Adds new node to the end of the list
    def append(self, new_data):
        if self.head is None:
            self.push(new_data)
        else:
            new_node = Node(new_data)
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            self.length += 1

    # Inserts new node at the specified position
    def insert(self, new_data, pos):
        if pos > self.length:
            print('Index out of range.')
        elif pos == 0:
            self.push(new_data)
        elif pos == self.length:
            self.append(new_data)
        else:
            count = 1
            curr = self.head
            next = curr.next
            while count < pos:
                curr = next
                next = curr.next
                count += 1
            new_node = Node(new_data)
            new_node.next = next
            curr.next = new_node

            # ALTERNATIVELY
            # count = 0
            # curr = self.head
            # prev = None
            # while count < pos:
            #     prev = curr
            #     curr = curr.next
            #     count += 1
            # new_node = Node(new_data)
            # new_node.next = curr
            # prev.next = new_node

            self.length += 1

    # Deletes the first occurrence of the given value
    def delete(self, val):
        curr = self.head
        if curr is None:
            print('Value not found.')
        else:
            if curr.data == val:
                self.head = curr.next
            else:
                prev = None
                while curr is not None and curr.data != val:
                    prev = curr
                    curr = curr.next
                if curr is not None:
                    prev.next = curr.next
                else:
                    print('Value not found.')

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
