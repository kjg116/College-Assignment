def main():
    keep_going = "y"

    def palindrome():
        if x_reversed == x:
            print("It is a Palindrome!")
        else:
            print("It is not a Palindrome")

    while keep_going != "0":
        x = int(input("Please enter a 5 digit number: "))
        x_reversed = int(str(x)[::-1])
        print("")
        while x < 10000 or x > 100000:
            x = int(input("ERROR. Please enter a five digit number: "))
            x_reversed = int(str(x)[::-1])
            print("")
        palindrome()

        print("")

        keep_going = input("Do you want to check another number? (0 to quit): ")

        print("")

main()


