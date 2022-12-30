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

# insert a new node at the beginning of the linked list
    def insert(self, value):
        self.head = Node(value, self.head)
        # Written step by step:
        # node_to_insert = Node(value)
        # old_head = self.head
        # self.head = node_to_insert
        # self.head.next = old_head

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

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def insert_before(self, value, new_value):
        current = self.head
        while current and current.next:
            if current.next.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return

            current = current.next

        raise TargetError(f"{value} is not in the linked list.")

    def insert_after(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return
            current = current.next

        raise TargetError(f"{value} is not in the linked list")


class TargetError(ValueError):
    pass
