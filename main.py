from typed_list import TypedList

def main():
    lst = TypedList()

    print("Initial Length:", lst.get_length())

    lst.append('A')
    lst.append('B')
    lst.append('C')

    print("Length after appending:", lst.get_length())

    lst.insert('X' + str(1), 1)
    lst.insert('Y' + str(1), 3)

    print("List after insertion:", lst)

    deleted_item = lst.delete(2)
    print("Deleted item:", deleted_item)
    print("List after deletion:", lst)

    lst.deleteAll('B')
    print("List after deleting all 'B':", lst)

    item = lst.get(0)
    print("Item at index 0:", item)

    cloned_list = lst.clone()
    print("Cloned list:", cloned_list)

    lst.reverse()
    print("Reversed list:", lst)

    index = lst.findFirst('X1')
    print("Index of first 'X1':", index)

    index = lst.findLast('Y1')
    print("Index of last 'Y1':", index)

    lst.clear()
    print("List after clearing:", lst)

    lst.extend(['D', 'E', 'F'])
    print("List after extending:", lst)

if __name__ == "__main__":
    main()
