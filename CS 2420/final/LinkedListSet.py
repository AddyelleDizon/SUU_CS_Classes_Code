from LinkedList import LinkedList

# Extend LinkedList
class LinkedListSet(LinkedList):
    
    def __init__(self):
        # Accesses the parent, LinkedList
        super().__init__()

    # Adds only unique items
    def unique_add(self, item):
        if not self.search(item):
            super().add(item)

    # Calls the new override add function
    def add(self, item):
        self.unique_add(item)

    # Calls the new override append function
    def append(self, item):
        if not self.search(item):
            super().append(item)

    # Calls the new override insert function
    def insert(self, posn, item):
        if not self.search(item):
            super().insert(posn, item)

    def Union(LLSet1, LLSet2):
        current = LLSet1.head
        total = LinkedListSet()

        while current:
            total.add(current.data)
            current = current.next

        current = LLSet2.head

        while current:
            total.add(current.data)
            current = current.next
        return total

    def Intersection(LLSet1, LLSet2):
        current = LLSet1.head
        total = LinkedListSet()

        while current:
            if LLSet2.search(current.data):
                total.add(current.data)
            current = current.next
        return total

    def Difference(LLSet1, LLSet2):
        current = LLSet1.head
        total = LinkedListSet()
        
        while current:
            if not LLSet2.search(current.data):
                total.add(current.data)
            current = current.next
        return total