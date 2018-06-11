def main():

    open_file1 = open("lowercase.txt", 'w')
    open_file2 = open("uppercase.txt", "w")
    open_file3 = open("mixCase.txt", 'w')
    open_file4 = open('alphaNum.txt', 'w')
    open_file5 = open('numbers.txt', 'w')

    try:
        open_file = open(input("Enter filename: "), 'r')
    except FileNotFoundError:
        print("Error: file could not be opened")

    list = []

    for lines in open_file:
        items = lines.rstrip().split()
        list.append(items)


    print()

    for word in list:
       for words1 in word:
           x = words1.rstrip(".").rstrip(",").rstrip("!")
           if x.isalnum() == True and x.isdigit() == False and x.isalpha() == False:
               open_file4.write(x + '\n')
           elif x.isdigit() == True:
               open_file5.write(x + '\n')
           elif x.isupper() == True:
               open_file2.write(x + '\n')
           elif x.islower() == True:
               open_file1.write(x + '\n')
           else:
               open_file3.write(x + '\n')

    open_file.close()
    open_file1.close()
    open_file2.close()
    open_file3.close()
    open_file4.close()
    open_file5.close()


main()
