"""
Carlos Romero

CS 3035-05(13119)

Exercise: Binary Search

Due on the 30th of March
"""


def binary_search(list, target):
    if (len(list) < 1):
        return 1

    low = 0
    high = len(list) - 1
    print("Searching " + str(list) + " for " + str(target))

    while low <= high:
        print("Comparing " + str(target) + " and " + str(list[high]))

        mid = int ((low + high) / 2 )
        if (list[mid] == target):
            return mid

        if (list[mid] < target):
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():

    empty_list, target_a  = [], 1
    small_list, target_b  = [1, 3, 5, 6, 9], 6
    medium_list, target_c = [1, 2, 4, 5, 8, 12, 15], 5
    big_list, target_d    = [2, 4, 7, 9, 13, 14, 16, 18, 19], 14

    print(binary_search(small_list, target_b))


main()