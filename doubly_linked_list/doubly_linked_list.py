from typing import Optional

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    """Each Node holds a reference to its prev_nodeious node
    as well as its next_node node in the List."""
    class _Node:
        def __init__(self, value, prev_node: Optional[DoublyLinkedList._Node] = None, next_node: Optional[DoublyLinkedList._Node] = None):
            self.value = value
            self.prev_node = prev_node
            self.next_node = next_node

        """Wrap the given value in a DoublyLinkedList._Node and insert it
        after this node. Note that this node could already
        have a next_node node it is point to."""
        def insert_after(self, value):
            current_next_node = self.next_node
            self.next_node = DoublyLinkedList._Node(value, self, current_next_node)
            if current_next_node:
                current_next_node.prev_node = self.next_node

        """Wrap the given value in a DoublyLinkedList._Node and insert it
        before this node. Note that this node could already
        have a prev_nodeious node it is point to."""
        def insert_before(self, value):
            current_prev_node = self.prev_node
            self.prev_node = DoublyLinkedList._Node(value, current_prev_node, self)
            if current_prev_node:
                current_prev_node.next_node = self.prev_node

        """Rearranges this DoublyLinkedList._Node's prev_nodeious and next_node pointers
        accordingly, effectively deleting this DoublyLinkedList._Node."""
        def delete(self):
            if self.prev_node:
                self.prev_node.next_node = self.next_node
            if self.next_node:
                self.next_node.prev_node = self.prev_node


    def __init__(self, node: Optional[DoublyLinkedList._Node]=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a DoublyLinkedList._Node and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's prev_nodeious pointer accordingly."""
    def add_to_head(self, value):
        pass

    """Removes the List's current head node, making the
    current head's next_node node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        pass

    """Wraps the given value in a DoublyLinkedList._Node and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next_node pointer accordingly."""
    def add_to_tail(self, value):
        pass

    """Removes the List's current tail node, making the 
    current tail's prev_nodeious node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node: DoublyLinkedList._Node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node: DoublyLinkedList._Node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node: DoublyLinkedList._Node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
