def main():
    keep_going = "y"

    def palindrome():
        if number == x:
            print(number, "this is a palindrome!")

    while keep_going != "0":

        num1 = int(input('Please enter a number between 100 and 1000: '))

        while num1 >= 1000 or num1 <= 100:
            print("")
            num1 = int(input('ERROR. Please enter a number between 100 and 1000: '))

        print("")

        num2 = int(input('Please enter a number between 100 and 1000: '))

        while num2 >= 1000 or num2 <= 100:
            print("")
            num2 = int(input('ERROR. Please enter a number between 100 and 1000: '))

        print("")

        bigX = num2
        littleX = num1

        if num1 > num2:
            bigX = num1
            littleX = num2

        for number in range(littleX, bigX):
            primes = 0

            for each in range(2, number - 1):
                if number % each == 0:
                    primes = 1
            if primes == 0:
                palindrome()
            if number != x:
                print("None of the primes in this range are palindromes.")

        print("")

        keep_going = input("Do you want to check another number? (0 to quit): ")

        print("")

main()


