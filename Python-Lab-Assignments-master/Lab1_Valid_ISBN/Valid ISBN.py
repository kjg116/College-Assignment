def ISBN():
    user_num = input("Please input an ISBN number: ")

    #removes "-" from string
    user_num = user_num.replace('-', '')

    user_list = []

    #places all strings into a list and turns them into integers
    for items in user_num:
        y = int(items)
        user_list.append(y)

    print("")

    #equation to validate ISBN
    x = (user_list[0] + (user_list[1] * 3) + user_list[2] + (user_list[3] * 3) + user_list[4]+ (user_list[5] * 3) + user_list[6]+ (user_list[7] * 3) + user_list[8]+ (user_list[9] * 3) + user_list[10]+ (user_list[11] * 3))

    y = x % 10

    #checks to see if equation equals check number
    if 10 - y == user_list[12]:
        print(user_num, "is a valid ISBN")
    elif 10 - y == 10 and user_list[12] == 0:
        print(user_num, "is a valid ISBN")
    else:
        print(user_num, "is not a valid ISBN")

ISBN()
