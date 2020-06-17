from typing import Optional

class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.nextNode: Node = None

    def __init__(self, items=None): # set items to be an optional generic list 
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

        if items is not None and len(items) > 0:
            items_iter = iter(items)
            self.head = self.Node(next(items_iter))
            self.tail = self.head
            current: Node = self.head
            for item in items_iter:
                current.nextNode = self.Node(item)
                current = current.nextNode
            self.tail = current

    def add_to_tail(self):
        pass

    def contains(self, needle):
        pass

    def remove_head(self):
        pass

    def get_max(self):
        pass

    # here is a long way of making an iterator
    # def __iter__(self):
    #     owner: LinkedList = self
    #     class SinglyLinkedListIter:
    #         def __init__(self):
    #             self.__current: Node = owner.head

    #         def __iter__(self):
    #             return self

    #         def __next__(self):
    #             while True:
    #                 if self.__current is None:
    #                     raise StopIteration
    #                 self.__next_value = self.__current.value
    #                 self.__current = self.__current.nextNode
    #                 return self.__next_value
    #     return SinglyLinkedListIter()

    # here is a much shorter way
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.nextNode

    def __str__(self):
        result = [item for item in self]
        return str(result)
