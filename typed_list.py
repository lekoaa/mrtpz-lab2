class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TypedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_length(self):
        return self.length
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, item, index):
        if index < 0 or index > self.length:
            raise ValueError("Invalid index")

        new_node = Node(item)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif index == self.length:
                new_node.next = self.head
                self.tail.next = new_node
                self.tail = new_node
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                new_node.next = current.next
                current.next = new_node

        self.length += 1


    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if self.length == 1:
            deleted_item = self.head.data
            self.head = None
            self.tail = None
        elif index == 0:
            deleted_item = self.head.data
            self.head = self.head.next
            self.tail.next = self.head
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            deleted_item = current.next.data
            current.next = current.next.next
            if index == self.length - 1:
                self.tail = current
        self.length -= 1
        return deleted_item


    def deleteAll(self, item):
        if self.length == 0:
            return "Item not found"

        current = self.head
        prev = None
        deleted = False

        while current is not self.tail:
            if current.data == item:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                if current == self.tail:
                    self.tail = prev

                self.length -= 1
                deleted = True
            else:
                prev = current
            
            current = current.next
        
        if self.tail.data == item:
            if prev is None:
                self.head = self.tail.next
            else:
                prev.next = self.tail.next

            self.length -= 1
            deleted = True

        if deleted is True:
            return None
        else:
            return "Item not found"

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self):
        cloned_list = TypedList()
        current = self.head
        for _ in range(self.length):
            cloned_list.append(current.data)
            current = current.next
        return cloned_list

    def reverse(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        while current.next != self.head:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        current.next = prev
        self.head = current

    def findFirst(self, value):
        current = self.head
        for i in range(self.length):
            if current.data == value:
                return i
            current = current.next
        return -1

    def findLast(self, value):
        current = self.head
        index = -1
        for i in range(self.length):
            if current.data == value:
                index = i
            current = current.next
        return index

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def extend(self, other_list):
        for item in other_list:
            self.append(item)
    
    def get_list(self):
        if self.length == 0:
            return []

        items = []
        current = self.head
        items.append(current.data)

        while current.next != self.head:
            current = current.next
            items.append(current.data)

        return items

    def __str__(self):
        if self.length == 0:
            return "[]"
        elements = []
        current = self.head
        for _ in range(self.length):
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"    