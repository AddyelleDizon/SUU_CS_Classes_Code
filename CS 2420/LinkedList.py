from Node import Node

class LinkedList:
    """A list of (non-sorted) items"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    # Homework;                                             Notes are for myself to review for exam

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

    def append(self, item):
        temp = Node(item)                                   # Creates a node, item is data
        if not self.head:                                   # Checks if the self.head is empty
            self.head = temp                                # If empty, set self.head to as new node and return
            return   
        current = self.head                                 # Set current to self.head, go through the list using the while loop
        while current.next:                                 # Loop stops when the current.next = None
            current = current.next
        current.next = temp                                 # Since current.next = None, it'll end the list (from previous if statement)

    def index(self, item):
        current = self.head
        position = 0                                        # Tracks the index; starts at 0
        while current:                                      # Iterate through the list using the while loop
            if current.data == item:                        # If the current.data == item, return the current position
                return position                 
            current = current.next                          # Set the head node to be the next node
            position += 1                                   # Increase position
        raise ValueError("Item not found in the list")      # If loop ends without finding item, raise valueError

    def insert(self, posn, item):
        if posn == 0:                                       # If we insert at the position 0, set the new node as the head
            temp = Node(item)                               # If not, iterate to next item on list
            temp.next = self.head                           
            self.head = temp
            return
        
        current = self.head
        posnCounter = 0                                     # Counter for current position

        while current and posnCounter < posn - 1:           # While the self.head and the position counter is less than the position - 1, 
            current = current.next                          # add to the counter and iterate
            posnCounter += 1 
        if not current:
            raise ValueError("Position does not exist")     # If position is out of bounds, raise a ValueError
        
        temp = Node(item)                       
        temp.next = current.next
        current.next = temp

    def pop(self):
        if not self.head:
            raise ValueError("List is empty")               # If the list is empty, rasie a ValueError
        
        if not self.head.next:                              # If there's only one item (no head's next node), remove and return the value
            data = self.head.data                           
            self.head = None                                
            return data                                     
         
        current = self.head                                  

        while current.next.next:                            # Iterate until the second to last node (next's next node)
            current = current.next                          # Remove the lats node and return data
        data = current.next.data                              
        current.next = None                                
        return data                                           

    def pop_at_position(self, posn):                        # Combination of pop() and insert() functions
        if not self.head:
            raise ValueError("List is empty")
        
        if posn == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        
        current = self.head
        position = 0

        while current.next and position < posn - 1:
            current = current.next
            position += 1

        if not current.next:
            raise ValueError("Position out of bounds")
        
        data = current.next.data
        current.next = current.next.next
        return data


