from typed_list import TypedList


def main():

    my_list = TypedList()

    my_list.add(10)
    my_list.add(20)
    my_list.add(30)

    print(f"Size of the list: {my_list.size()}")

    item = my_list.get(1)
    if item is not None:
        print(f"Item at index 1: {item}")

    my_list.remove(20)

    print(f"Size of the list after removal: {my_list.size()}")


if __name__ == "__main__":
    main()