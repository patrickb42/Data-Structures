from typing import Optional, List
from queue import Queue, Empty
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

    def __iter__(self):
        return self.make_in_order_iter()

    def __str__(self):
        return str(list(self))

    def __contains__(self, needle):
        return self.contains(needle)

    def make_in_order_iter(self):
        return BSTNode._Iter(self, in_order=True)

    def make_pre_order_iter(self):
        return BSTNode._Iter(self, pre_order=True)

    def make_post_order_iter(self):
        return BSTNode._Iter(self, post_order=True)

    def make_breadth_first_iter(self):
        return BSTNode._Iter(self, breadth_first=True)

    class _Iter:
        def __init__(
                self,
                head,
                in_order=False,
                pre_order=False,
                post_order=False,
                breadth_first=False,
        ):
            counter = 0
            counter += 1 if in_order else 0
            counter += 1 if pre_order else 0
            counter += 1 if post_order else 0
            counter += 1 if breadth_first else 0
            if counter == 0:
                in_order = True
            elif counter != 1:
                raise Exception('must provide only one traversal flag for BSTNode iter')

            self.__in_order = in_order
            self.__pre_order = pre_order
            self.__post_order = post_order
            self.__breadth_first = breadth_first
            self.__parents: List[BSTNode] = []
            self.__searched_left = False
            self.__searched_right = False
            self.__current_node = head

            if in_order:
                self.__step = self.__step_in_order
                self.__returned_head = False
            elif pre_order:
                self.__step = self.__step_pre_order
                self.__returned_last_value = False
            elif post_order:
                self.__step = self.__step_post_order
                self.__post_order_head_returned = False
            elif breadth_first:
                self.__step = self.__step_breadth_first
                self.__node_queue = Queue()
                self.__last_node_returned = False

        def __iter__(self):
            return self

        def __next__(self):
            return self.__step()

        def __go_left(self):
            self.__parents.append(self.__current_node)
            self.__current_node = self.__current_node.left
            self.__searched_left = False
            self.__searched_right = False

        def __go_right(self):
            self.__parents.append(self.__current_node)
            self.__current_node = self.__current_node.right
            self.__searched_left = False
            self.__searched_right = False

        def __dive_left(self):
            while self.__current_node.left is not None:
                self.__go_left()

        def __return_to_parent(self):
            if len(self.__parents) == 0:
                raise StopIteration
            self.__searched_left = True
            self.__searched_right = True if self.__current_node is self.__parents[-1].right else False
            self.__current_node = self.__parents.pop()

        def __step_in_order(self):
            if not self.__searched_left:
                self.__dive_left()
            elif self.__current_node.right is not None:
                self.__go_right()
                self.__dive_left()
            else:
                self.__searched_right = True
                if not self.__returned_head and len(self.__parents) == 0:
                    self.__returned_head = True
                    return self.__current_node.value
                while self.__searched_right:
                    self.__return_to_parent()
            self.__searched_left = True
            return self.__current_node.value

        def __step_pre_order(self):
            return_value = self.__current_node.value
            while True:
                if self.__current_node.left is not None and not self.__searched_left:
                    self.__go_left()
                    break
                elif self.__current_node.right is not None and not self.__searched_right:
                    self.__go_right()
                    break
                else:
                    try:
                        self.__return_to_parent()
                    except StopIteration:
                        if not self.__returned_last_value:
                            self.__returned_last_value = True
                            break
                        raise
            return return_value

        def __step_post_order(self):
            while not self.__searched_left or not self.__searched_right:
                self.__searched_left = True if self.__current_node.left is None else self.__searched_left
                self.__searched_right = True if self.__current_node.right is None else self.__searched_right
                if not self.__searched_left:
                    self.__dive_left()
                elif not self.__searched_right:
                    self.__go_right()
                    self.__dive_left()
            return_value = self.__current_node.value
            if not self.__post_order_head_returned and len(self.__parents) == 0:
                self.__post_order_head_returned = True
            else:
                self.__return_to_parent()
            return return_value

        def __step_breadth_first(self):
            return_value = self.__current_node.value
            if self.__current_node.left is not None:
                self.__node_queue.put(self.__current_node.left)
            if self.__current_node.right is not None:
                self.__node_queue.put(self.__current_node.right)
            try:
                self.__current_node = self.__node_queue.get(False)
            except Empty:
                if self.__last_node_returned:
                    raise StopIteration
                self.__last_node_returned = True
            return return_value

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, needle):
        current_node = self
        while True:
            if needle == current_node.value:
                return True
            elif needle < current_node.value:
                if current_node.left is None:
                    return False
                current_node = current_node.left
            else:
                if current_node.right is None:
                    return False
                current_node = current_node.right

    # Return the maximum value found in the tree
    def get_max(self):
        return max(self)

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        for value in self:
            fn(value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        for i in node:
            print(i)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        for i in node.make_breadth_first_iter():
            print(i)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        for i in node.make_pre_order_iter():
            print(i)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        for i in node.make_pre_order_iter():
            print(i)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        for i in node.make_post_order_iter():
            print(i)


if __name__ == "__main__":
    # node1 = BSTNode(1)
    # node2 = BSTNode(2)
    # node3 = BSTNode(3)
    # node4 = BSTNode(4)
    # node5 = BSTNode(5)
    # node6 = BSTNode(6)
    # node7 = BSTNode(7)
    # node8 = BSTNode(8)
    # node9 = BSTNode(9)
    # node10 = BSTNode(10)
    # HEAD = node4
    # node2.left = node1
    # node2.right = node3
    # node4.left = node2
    # node6.left = node5
    # node8.right = node9
    # node7.right = node8
    # node10.left = node7
    # node6.right = node10
    # node4.right = node6
    # print(HEAD)
    # print(BSTNode(5))
    #
    # bst = BSTNode(1)
    # bst.insert(8)
    # bst.insert(5)
    # bst.insert(7)
    # bst.insert(6)
    # bst.insert(3)
    # bst.insert(4)
    # bst.insert(2)
    # print(bst)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #       4
    #      / \
    #     /   \
    #    /     \
    #   2       6
    #  / \     / \
    # 1   3   5   10
    #            /
    #           7
    #            \
    #             8
    #              \
    #               9
    pass
