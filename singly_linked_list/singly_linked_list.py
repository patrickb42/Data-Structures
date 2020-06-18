from typing import Optional, List

class SinglyLinkedList:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.next_node: Optional[SinglyLinkedList._Node] = None

    def __init__(self, items: Optional[List]=None): # set items to be an optional generic list 
        self.head: Optional[SinglyLinkedList._Node] = None
        self.tail: Optional[SinglyLinkedList._Node] = None
        self.length: int = len(items) if items is not None else 0

        if items is not None and len(items) > 0:
            items_iter = iter(items)
            self.head = SinglyLinkedList._Node(next(items_iter))
            self.tail = self.head
            current: SinglyLinkedList._Node = self.head
            for item in items_iter:
                current.next_node = SinglyLinkedList._Node(item)
                current = current.next_node
            self.tail = current

    def add_to_tail(self, item):
        if self.tail is not None:
            self.tail.next_node = SinglyLinkedList._Node(item)
            self.tail = self.tail.next_node
        else:
            self.head = SinglyLinkedList._Node(item)
            self.tail = self.head
        self.length += 1

    def contains(self, needle):
        return needle in self

    def remove_head(self):
        return_value = None
        if self.head is not None:
            return_value = self.head.value
            self.head = self.head.next_node
            self.length -= 1
            if self.length < 2:
                self.tail = self.head
        return return_value

    def get_max(self):
        return max(self) if self.length > 0 else None

    # here is a long way of making an iterator
    # def __iter__(self):
    #     owner: SinglyLinkedList = self
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
    #                 self.__current = self.__current.next_node
    #                 return self.__next_value
    #     return SinglyLinkedListIter()

    # here is a much shorter way
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next_node

    def __str__(self) -> str:
        return str(list(self))

    def __len__(self) -> int:
        return self.length

if __name__ == "__main__":
    thing = SinglyLinkedList([1, 2, 3])
    print(3 in thing)
    print(thing.get_max())
    print(thing)
