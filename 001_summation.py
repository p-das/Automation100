def sum_of_numbers(*args):
    sum1 = 0
    for i in args:
        sum1 = sum1+i
    return sum1

two_num = sum_of_numbers(13,14)
print(two_num)

three_num = sum_of_numbers(13,14,15)
print(three_num)