"""
This module offer LinkedList implementation in Python.
"""


class Node:
    """
    This class allows to create nodes for future LinkedList.
    """
    def __init__(self, data=None, next: "Node" = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    """
    This class implemets a LinkedList data structure in Python.
    This implementation allows to create empty LinkedList only.
    To populate it - just use 'add' method.
    Each LikedList contains head node (accessed with 'head' property),
    tail node (accessed with 'tail' property) and
    length of whole LinkedList (accessed with 'length' property).
    """

    __slots__ = ("__head", "__tail", "__length")

    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__length: int = 0

    def add(self, node: Node, position="end"):
        """
        'position' argument only to be 'start', 'end' or integer between 0 and self.__length
        """
        if position not in ("start", "end") and not (
            type(position) == int and 0 <= position <= self.__length
        ):
            raise ValueError(
                f"\n'position' argument only to be 'start', 'end' or integer between 0 and {self.__length}"
            )
        if not isinstance(node, Node):
            raise TypeError("'node' must be a Node instance only.")

        if not self.__head:
            self.__head = node
        else:
            if position == "end" or position == self.__length:
                if self.__tail:
                    node.next = self.__tail.next
                    self.__tail.next = node
                self.__tail = node
            elif position == "start" or position == 0:
                node.next = self.__head
                self.__head = node
            else:
                node_prev = self.__head
                for _ in range(position - 1):
                    node_prev = node_prev.next
                node.next = node_prev.next
                node_prev.next = node

        self.__length += 1

        print(f"Added one node.\nLlist length is {self.length}.")

    def __str__(self) -> str:
        """
        Print whole LinkedList in a row.
        """
        node_start = self.__head
        printllist = "["
        for _ in range(self.__length):
            if _ == self.__length - 1:
                printllist += f"{node_start}]"
            else:
                printllist += f"{node_start} -> "
            node_start = node_start.next
        return printllist

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def length(self):
        return self.__length


def main():
    
    node = Node("a")
    node1 = Node("b")
    node2 = Node("c")
    node3 = Node("d")
    node4 = Node("e")
    node5 = Node("f")

    node.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None  # default on creation

    llist = LinkedList()

    llist.add(node)
    llist.add(node1)
    llist.add(node2)
    llist.add(node3)
    llist.add(node4)
    llist.add(node5)

    print(llist.length)

    llist.add(Node('new_data'), 2)

    print(llist)


if __name__ == "__main__":
    main()
