class TypedList:
    def __init__(self):
        self.data = []  # Масив для зберігання даних

    def add(self, item):
        # Додавання елемента до списку
        self.data.append(item)

    def remove(self, item):
        # Видалення елемента зі списку
        if item in self.data:
            self.data.remove(item)

    def get(self, index):
        # Отримання елемента за індексом
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None

    def size(self):
        # Отримання розміру списку
        return len(self.data)
