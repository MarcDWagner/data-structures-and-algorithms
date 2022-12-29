class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None, values=None):
        self.head = head

    def __iter__(self):
        def value_create():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_create()

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        current = self.head
        output = ""
        while current:
            node_str = "{ " + current.value + " } -> "
            output += node_str
            current = current.next
        return output + "NULL"

