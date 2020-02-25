from math import floor


def b_search(num, target):
    left = 0
    right = len(num) - 1
    while left <= right:
        mid = floor((left + (right - 1) / 2))
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


li = [1, 4, 7, 8, 9, 10, 15]
print(b_search(li, 4))
