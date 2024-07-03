def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst):
    input_value = input("Enter a value to append to the list: ")
    lst.append(input_value)
    print("Updated list is:", lst)


def handle_extend(lst):
    input_value = input("Enter needed values to extend the list with (comma-separated): ").split(",")
    lst.extend(input_value)
    print("Updated list is:", lst)


def handle_insert(lst):
    input_index = int(input("Enter needed index to insert needed value at: "))
    if 0 <= input_index < len(lst):
        input_value = input("Enter needed value to insert at needed index: ")
        lst.insert(input_index, input_value)
    else:
        print("You've entered an invalid index!")
    print("Updated list is:", lst)


def handle_remove(lst):
    input_value = input("Enter needed value to remove it from the list: ")
    if input_value in lst:
        lst.remove(input_value)
    else:
        print("Value not found in the list!")
    print("Updated list is:", lst)


def handle_pop(lst):
    input_index = input("Enter needed index to pop it from the list: ")
    if input_index == "":
        lst.pop()
    elif input_index:
        integer_index = int(input_index)
        if integer_index < len(lst):
            lst.pop(integer_index)
        else:
            print("Index out of range!")
    print("Updated list is:", lst)


def handle_clear(lst):
    lst.clear()
    print("Updated list is:", lst)


def handle_index(lst):
    input_value = input("Enter needed value to find its index: ")
    if input_value not in lst:
        print("Value not found in the list!")
    else:
        needed_index = lst.index(input_value)
        print("The index of the value is:", needed_index)


def handle_count(lst):
    input_value = input("Enter needed value to find its count in the list: ")
    value_count = lst.count(input_value)
    print("The count of the value is:", value_count)


def handle_sort(lst):
    lst.sort()
    print("Updated list is:", lst)


def handle_reverse(lst):
    lst.reverse()
    print("Updated list is:", lst)


def handle_copy(lst):
    lst.copy()
    print("Copied list is:", lst)


def main():
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()