"""
Carlos Romero

CS 3035-05(13119)

Exercise: Python Recursion

Due on the 28th of March
"""


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


def count(string):
    if not string:
        # checking if the length of the string is zero meaning if no string exists
        return 0
    return 1 + count(string[1:])


def reverse(string):

    if not string:
        # an empty string is the same in reversed order
        return ""
    return string[-1] + reverse(string[:-1])


def palindrome(string):
    clensed_string = "".join(word.lower() for word in string if word.isalpha())

    # if string is a single character or empty it is palindrome
    if len(clensed_string) <= 1:
        return True

    # case: first need to check if the outside characters are the same
    if clensed_string[0] != clensed_string[-1]:
        return False
    # follow through with recursion
    else:
        return palindrome(clensed_string[1:-1])


def run_count_reverse():
    user_input = input("Enter a string: ")
    result = count(user_input)
    resultReverse = reverse(user_input)
    result_palindrome = palindrome(user_input)

    print("")
    print(f"The length of the string is: {result}")
    print(f"The reverse of the string is: {resultReverse}")
    print(f"The palindrome of the string is: {result_palindrome}")


run_count_reverse()
