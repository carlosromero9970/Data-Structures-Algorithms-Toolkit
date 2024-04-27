def mergesort(list):
    if len(list) <= 1:
        return list

    # floor division
    half = len(list) // 2

    left = list[:half]
    right = list[half:]

    left = str(mergesort(left))
    right = str(mergesort(right))

    return merge(left, right)


def merge(left_list, right_list):
    if not left_list:
        return right_list

    if not right_list:
        return left_list

    if left_list[0] < right_list[0]:
        return left_list[0] + merge(left_list[1:], right_list)
    else:
        return right_list[0] + merge(left_list, right_list[1:])


# print(16 // 4)
print(mergesort([]))
print(mergesort([-1]))
print(mergesort([5, -1]))
print(mergesort([5, -1, 42]))
print(mergesort([5, -1, 42, -1000]))

print(mergesort([""]))
print(mergesort(["Godzilla"]))
print(mergesort([" ", "Godzilla"]))
print(mergesort(["Mothra", "Godzilla"]))
print(mergesort(["Mothra", "Godzilla", "Jersey Devil"]))
print(mergesort(["Mothra", "Loch Ness Monster", "Godzilla", "Jersey Devil"]))


