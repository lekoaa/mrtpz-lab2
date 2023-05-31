class TypedList:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def length(self):
        return len(self.data)
    
    def append(self, element):
        self.data.append(element)

    def insert(self, element, index):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, element)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data.pop(index)
        
    def deleteAll(self, element):
        self.data = [item for item in self.data if item != element]

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def clone(self):
        return TypedList(self.data[:])
    
    def reverse(self):
        self.data = self.data[::-1]

    def findFirst(self, element):
        for i in range(len(self.data)):
            if self.data[i] == element:
                return i
        return -1
    
    def findLast(self, element):
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == element:
                return i
        return -1

    def clear(self):
        self.data = []

    def extend(self, elements):
        self.data.extend(elements)
