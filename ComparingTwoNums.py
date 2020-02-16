def compare_two_nums(num1, num2):
    if num1 ^ num2 != 0:
        return False
    else:
        return True


print(compare_two_nums(4, 4))  # true
print(compare_two_nums(3, 4))  # false
