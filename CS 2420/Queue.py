from Node import Node

class Queue:
    """Queue implementation using Nodes"""

    def __init__(self):
        self.head = None

    def __str__(self):
        strList = "["                                       # Create start of bracket list, [
        current = self.head                                 # Set the self.head to current, iterating through list (doesn't modify the self.head)
        while current:                                      # While it's self.head, 
            strList += str(current.data)                    # Appends the string to the list
            if current.next:
                strList += ", "                             # Adds a comma and space
            current = current.next
        strList += "]"                                      # Ends list with ] and returns it
        return strList

    def enqueue(self, item):
        temp = Node(item)                                   # Creates a node, item is data
        if not self.head:                                   # Checks if the self.head is empty
            self.head = temp                                # If empty, set self.head to as new node and return
            return   
        current = self.head                                 # Set current to self.head, go through the list using the while loop
        while current.next:                                 # Loop stops when the current.next = None
            current = current.next
        current.next = temp  

    def dequeue(self):
        if not self.head:
            raise ValueError("List is empty")               # If the list is empty, rasie a ValueError
        if not self.head.next:                              # If there's only one item (no head's next node), remove and return the value
            data = self.head.data                           
            self.head = None                                
            return data                                     
        data = self.head.data 
        self.head = self.head.next                                                         
        return data

    def is_empty(self):
        return self.head == None

    def peek(self):
        if not self.head:
            return None
        data = self.head.data
        return data

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count
