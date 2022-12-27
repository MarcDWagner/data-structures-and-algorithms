class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self):
        self.head = None


first_node = Node("a")
second_node = Node("b")
third_node = Node("c")

link_list = LinkedList()

link_list.head = first_node
first_node.next = second_node
second_node.next = third_node
