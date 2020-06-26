from typing import Optional, List

class DoublyLinkedListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node: Optional[DoublyLinkedListNode] = prev_node
        self.next_node: Optional[DoublyLinkedListNode] = next_node


    def insert_after(self, value):
        """Wrap the given value in a DoublyLinkedListNode and insert it
        after this node. Note that this node could already
        have a next_node node it is point to."""
        current_next_node = self.next_node
        self.next_node = DoublyLinkedListNode(value, self, current_next_node)
        if current_next_node is not None:
            current_next_node.prev_node = self.next_node

    def insert_before(self, value):
        """Wrap the given value in a Node and insert it
        before this node. Note that this node could already
        have a previous node it is point to."""
        current_prev_node = self.prev_node
        self.prev_node = DoublyLinkedListNode(value, current_prev_node, self)
        if current_prev_node is not None:
            current_prev_node.next_node = self.prev_node

    def delete(self):
        """Rearranges this Node's previous and next_node pointers
        accordingly, effectively deleting this DoublyLinkedListNode."""
        if self.prev_node is not None:
            self.prev_node.next_node = self.next_node
        if self.next_node is not None:
            self.next_node.prev_node = self.prev_node
        self.prev_node = None
        self.next_node = None

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    """Each Node holds a reference to its previous node
    as well as its next_node node in the List."""

    def __init__(self, items: Optional[List] = None):
        self.head: Optional[DoublyLinkedListNode] = None
        self.tail: Optional[DoublyLinkedListNode] = None
        self.length: int = 0

        if items is not None and len(items) != 0:
            items_iter = iter(items)
            self.head = DoublyLinkedListNode(next(items_iter))
            current_node: DoublyLinkedListNode = self.head
            for item in items_iter:
                current_node.insert_after(item)
                current_node = current_node.next_node
            self.tail = current_node
            self.length = len(items)

    def __len__(self):
        return self.length


    class _Node_Iter:
        def __init__(self, owner, iteration_reversed=False):
            self.__iteration_reversed = iteration_reversed
            self.__current_node: Optional[DoublyLinkedListNode] = (owner.head) if not iteration_reversed else (owner.tail)

        def __iter__(self):
            return self

        def __next__(self) -> DoublyLinkedListNode:
            if self.__current_node is not None:
                next_node = self.__current_node
                self.__current_node = (self.__current_node.next_node) if not self.__iteration_reversed else (self.__current_node.prev_node)
                return next_node
            raise StopIteration


    class _Value_Iter(_Node_Iter):
        def __init__(self, owner, iteration_reversed=False):
            super().__init__(owner, iteration_reversed)
        
        def __iter__(self):
            return self
            
        def __next__(self):
            return super().__next__().value


    def __iter__(self):
        return DoublyLinkedList._Value_Iter(self)
    
    def make_reversed_iter(self):
        return DoublyLinkedList._Value_Iter(self, iteration_reversed=True)

    def __get_node(self, index: int) -> DoublyLinkedListNode:
        if not self.__is_valid_index(index):
            raise IndexError
        iteration_reversed = self.__should_reverse_search(index)
        normalize_index = self.__normalize_index(index)
        for i, node in enumerate(DoublyLinkedList._Node_Iter(self, iteration_reversed)):
            if(i == normalize_index):
                return node

    def get(self, index: int):
        return self.__get_node(index).value

    def __should_reverse_search(self, index: int) -> bool:
        # return False
        return ((len(self) // 2) <= index) if index >= 0 else (len(self) // 2 > abs(index) - 1)

    def __is_valid_index(self, index: int):
        return (index < len(self) and index >= 0) or (abs(index) <= len(self) and index < 0)

    def __normalize_index(self, index):
        if self.__should_reverse_search(index):
            return (len(self) - 1 - index) if index >= 0 else (abs(index) - 1)
        else:
            return (index) if index >= 0 else (len(self) + index)

    def __str__(self):
        return str(list(self))

    def add_to_head(self, value):
        """Wraps the given value in a Node and inserts it
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly."""
        if self.head is None:
            self.head = DoublyLinkedListNode(value)
            self.tail = self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev_node
        self.length += 1
        self.tail = self.head if len(self) < 2 else self.tail

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next_node node the new head of the List.
        Returns the value of the removed Node."""
        return_value = None
        if self.head is not None:
            return_value = self.head.value
            self.head = self.head.next_node
            if self.head is not None:
                self.head.prev_node.delete()
            self.length -= 1
            self.tail = self.head if len(self) < 2 else self.tail
        return return_value

    def add_to_tail(self, value):
        """Wraps the given value in a Node and inserts it
        as the new tail of the list. Don't forget to handle 
        the old tail node's next_node pointer accordingly."""
        if self.tail is None:
            self.tail = DoublyLinkedListNode(value)
            self.head = self.tail
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next_node
        self.length += 1

    def remove_from_tail(self):
        """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node."""
        return_value = None
        if self.tail is not None:
            return_value = self.tail.value
            self.tail = self.tail.prev_node
            if self.tail is not None:
                self.tail.next_node.delete()
            self.length -= 1
            self.head = self.tail if len(self) < 2 else self.head
        return return_value

    def move_to_front(self, index: int):
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List."""
        if len(self) == 1:
            if index != 0:
                raise IndexError
            return
        node = self.__get_node(index)
        if node is self.head:
            return
        elif node is self.tail:
            self.remove_from_tail()
            self.length += 1
        else:
            node.delete()
        node.next_node = self.head
        node.next_node = self.head
        self.head.prev_node = node
        self.head = self.head.prev_node

    def move_to_end(self, index: int):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""
        if len(self) == 1:
            if not self.__is_valid_index(index):
                raise IndexError
            return
        node = self.__get_node(index)
        if node is self.tail:
            return
        elif node is self.head:
            self.remove_from_head()
            self.length += 1
        else:
            node.delete()
        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = self.tail.next_node

    def delete(self, index: int):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""
        node = self.__get_node(index)
        if node is self.head:
            self.head = self.head.next_node
        if node is self.tail:
            self.tail = self.tail.prev_node
        node.delete()
        self.length -= 1

    def get_max(self):
        """Returns the highest value currently in the list"""
        return max(self)

if __name__ == "__main__":
    # foo = DoublyLinkedList()
    # foo.add_to_tail(1)
    # print(f'head: {foo.head.value}, tail: {foo.tail.value}, length: {len(foo)}, str: {foo}')
    # foo.add_to_head(2)
    # print(f'head: {foo.head.value}, tail: {foo.tail.value}, length: {len(foo)}, str: {foo}')
    # foo.move_to_end(0)
    # print(f'head: {foo.head.value}, tail: {foo.tail.value}, length: {len(foo)}, str: {foo}')
    # foo.move_to_front(-1)
    # print(f'head: {foo.head.value}, tail: {foo.tail.value}, length: {len(foo)}, str: {foo}')
    # foo.remove_from_head()
    # print(f'head: {foo.head.value}, tail: {foo.tail.value}, length: {len(foo)}, str: {foo}')
    # foo.remove_from_tail()
    # print(f'head: {foo.head}, tail: {foo.tail}, length: {len(foo)}, str: {foo}')

    bar = DoublyLinkedList(range(10_000_000))
    for i in range(5):
        print(f'{bar.get(5_000_000):,}')
    for i in range(5):
        print(f'{bar.get(-2_500_000):,}')
