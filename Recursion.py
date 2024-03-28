"""
Carlos Romero

CS 3035-05(13119)

Exercise: Python Recursion

Due on the 28th of March
"""
import sys


def count(string):
    """
    string: carlos

    = 1 + count("arlos")
    = 1 + (1 + count("rlos"))
    = 1 + (1 + (1 + count("los")))
    = 1 + (1 + (1 + (1 + count("os"))))
    = 1 + (1 + (1 + (1 + (1 + count("s")))))
    = 1 + (1 + (1 + (1 + (1 + (1 + count(""))))))
    = 1 + (1 + (1 + (1 + (1 + (1 + 0)))))
    = 1 + (1 + (1 + (1 + (1 + 1))))
    = 1 + (1 + (1 + (1 + 2)))
    = 1 + (1 + (1 + 3))
    = 1 + (1 + 4)
    = 1 + 5
    = 6
    """

    if not string:
        # checking if the length of the string is zero meaning if no string exists
        return 0
    return 1 + count(string[1:])


def reverse(string):
    """
    string: carlos

    = s + reverse("carlo")
    = s + (o + reverse("carl"))
    = s + (o + (l + reverse("car")))

    and so on...

    = solrac
    """

    if not string:
        # an empty string is the same in reversed order
        return ""
    return string[-1] + reverse(string[:-1])


def palindrome(string):
    """
    string = "abaaba"

    half = 3      since the len() gives us 6

    string[:half] = string[:3]  starts at index zero stops on the index before half(3)
    string[half:] = string[3:]  starts on in the index of 3 with the rest of the following string

    """
    half = int(len(string) / 2)
    first_half = string[:half]
    second_half = string[half:]





def run_count_reverse():
    user_input = input("Enter a string: ")
    result = count(user_input)
    resultReverse = reverse(user_input)
    print("")
    print(f"The length of the string is: {result}")
    print(f"The reverse of the string is: {resultReverse}")
    # print(user_input[-1])
    # print(user_input[:-1])

run_count_reverse()
