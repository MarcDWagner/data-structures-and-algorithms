class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        # if nodes is not None:
        #     node = Node(value=nodes.pop())
        #     self.head = node
        #     for element in nodes:
        #         node.next = Node(value=element)
        #         node = node.next


    def insert(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current != None:
            return True
        current = current.next
        return False


    def __str__(self):
        return f" {self.value} -> "
        # node = self.head
        # nodes = []
        # while node is not None:
        #     nodes.append(node.value)
        #     node = node.next
        # nodes.append("None")
        # return " -> ".join(nodes)


    # def print_ll(self):
    #     current = self.head

        # while current:
        #     print(current.value)
        #     current = current.next

    # def visualize(self):
    #     node = self.head
    #     nodes = []
    #     while node is not None:
    #         nodes.append(node.value)
    #         node = node.next
    #
    #     nodes.append("None")
    #     print(" -> ".join(nodes))




# if __name__ == "__main__":
#     Node("apple")
    # insert("banana")
# ll_1 = LinkedList("apple")
# ll_1.head.next = Node("banana")
# ll_1.head.next.next = Node("cucumber")
# ll_1.visualize()
