from Node import Node
from LinkedList import LinkedList

class LinkedListIterator:
    """An iterator for the LinkedList class"""

    def __init__(self, list):
        self.head = None

    def size_of_list(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def get_beginning_node(self):
        if self.head is None:
            return None
        return self.head

    def get_ending_node(self):
        pass

    def get_node_at_current_location(self):
        pass

    def advance_to_next_node(self):
        pass

    def has_next_node(self):
        if self.head.next is None:
            return False
        else:
            return True

    def go_back_a_node(self):
        pass

    def has_previous_node(self):
        pass

    