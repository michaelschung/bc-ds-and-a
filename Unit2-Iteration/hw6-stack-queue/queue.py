'''
Mr. Chung
3/15: Queue – a LinkedList wrapper
'''

from linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.pop()

    def size(self):
        return self.list.size()

    def print(self):
        self.list.print()
