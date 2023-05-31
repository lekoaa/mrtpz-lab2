class TypedList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.items)
    
    def append(self, element):
        self.items.append(element)

    def insert(self, element, index):
        if index < 0 or index > len(self.items):
            raise IndexError("Invalid index")
        self.items.insert(index, element)

    def delete(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Invalid index")
        return self.items.pop(index)
        
    def deleteAll(self, element):
        self.items = [item for item in self.items if item != element]

    def get(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Invalid index")
        return self.items[index]

    def clone(self):
        return TypedList(self.items.copy())
    
    def reverse(self):
        self.items = self.items[::-1]

    def findFirst(self, element):
        for i in range(len(self.items)):
            if self.items[i] == element:
                return i
        return -1
    
    def findLast(self, element):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == element:
                return i
        return -1

    def clear(self):
        self.items = []

    def extend(self, elements):
        self.items.extend(elements)
