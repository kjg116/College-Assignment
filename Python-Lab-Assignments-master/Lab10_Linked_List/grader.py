from LinkedList import *
grade = 0

for choice in range(1, 10):

    print(grade)
    print(choice)

    if choice == 1:
        #test constructor and __str__
        my_list = LinkedList()
        #print(str(my_list))
        if str(my_list) == "None":
            grade += 20


    elif choice == 2:
        #test adding an element at the beginning of the list
        my_list = LinkedList()
        my_list.insert_front(5)
        my_list.insert_front(6)
        my_list.insert_front(7)
        print(my_list)
        if str(my_list) == "7, 6, 5":
            grade += 10

    elif choice == 3:
        #test adding an element at the end of an empty list and at the end of an existing list
        my_list = LinkedList()
        my_list.insert_end(5)
        my_list.insert_end(6)
        my_list.insert_end(7)
        #print(my_list)
        if str(my_list) == "5, 6, 7":
            grade += 10

    elif choice == 4:
        #test adding an element at a position of an empty list and into an existing list
        my_list = LinkedList()
        my_list.insert_position(5, 0)
        my_list.insert_position(6, 0)
        my_list.insert_position(10, 0)
        my_list.insert_position(2, 1)
        print(my_list)
        if str(my_list) == "10, 2, 6, 5":
            grade += 10

    elif choice == 5:
        #test removing from the front of an existing list, list is created using insert_front()
        my_list = LinkedList()
        my_list.insert_front(5)
        my_list.insert_front(6)
        my_list.insert_front(7)
        my_list.delete_front()
        #print(my_list)
        if str(my_list) == "6, 5":
            grade += 10

    elif choice == 6:
        #test removing the entire list and then adding one other element (insert front)
        my_list = LinkedList()
        my_list.insert_front(5)
        my_list.insert_front(6)
        my_list.insert_front(7)
        my_list.delete_list()
        my_list.insert_front(2)
        #print(my_list)
        if str(my_list) == "2":
            grade += 10

    elif choice == 7:
        #test removing the first instance of a data item when it is the first one in the list
        my_list = LinkedList()
        my_list.insert_front(5)
        my_list.insert_front(6)
        my_list.insert_front(7)
        my_list.delete_item(7)
        print(my_list)
        if str(my_list) == "6, 5":
            grade += 10

    elif choice == 8:
        #test removing the first instance of a data item when it is the last one in the list
        my_list = LinkedList()
        my_list.insert_front(5)
        my_list.insert_front(6)
        my_list.insert_front(7)
        my_list.delete_item(5)
        print(my_list)
        if str(my_list) == "7, 6":
            grade += 10

    elif choice == 9:
        #test removing the first instance of a data item when it is in the middle of a list
        my_list = LinkedList()
        my_list.insert_front(5)
        my_list.insert_front(6)
        my_list.insert_front(7)
        my_list.delete_item(6)
        print(my_list)
        if str(my_list) == "7, 5":
            grade += 10

print("You made: ", grade)
