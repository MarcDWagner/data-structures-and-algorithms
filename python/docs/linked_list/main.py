class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


first_node = Node("A")
second_node = Node("B")
third_node = Node("C")

link_list = LinkedList()

link_list.head = first_node
first_node.next = second_node
second_node.next = third_node
