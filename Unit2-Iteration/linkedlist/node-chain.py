'''
Mr. Chung
3/10: Practice with Nodes
'''

from node import Node

node1 = Node('ram')
node2 = Node('ranch')
node3 = Node('fire')
node4 = Node('computer')
node5 = Node('Mr. Chung')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
