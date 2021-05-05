'''
Mr. Chung
3/12: Stack – a LinkedList wrapper
'''

from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, val):
        self.list.add_front(val)

    def pop(self):
        return self.list.pop()

    def size(self):
        return self.list.size()

    def print(self):
        self.list.print()
