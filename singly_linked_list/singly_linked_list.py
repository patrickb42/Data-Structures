from typing import Union

class LinkedList:
    class Node:
        def __init__(self, value, nextNode: Node=None):
            self.value = value
            self.nextNode = nextNode
    def __init__(self):
        self.head: Union[Node, None]
        self.tail: Union[Node, None]

    def add_to_tail(self):
        pass

    def contains(self, needle):
        pass

    def remove_head(self):
        pass

    def get_max(self):
        pass
