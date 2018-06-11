Valid_ISBN
Python Lab Assignment 1

Checks to see if the ISBN inputted by the user is an valid ISBN-13

The program uses the last digit of the ISBN-13 to check against the result of the following equation:

a + [b * 3] + c + [d * 3] + e + [f * 3] + g + [h * 3] + i + [j * 3] + k + [l * 3]

The program returns "This is a valid ISBN" If the check digit equals the result mod 10.
