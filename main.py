#Pytest


#1
# def positive_or_negative(x):
#     if x > 0:
#         return 'positive'
#     elif x < 0:
#         return 'negative'
#     else:
#         return 'Zero'






#2
# def even_or_odd(x):
#     if x % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'






#3
# def count_digits(number):
#     count = len(str(abs(number)))
#     return count





#4
# def sum_list(x):
#     return sum(x)





#5
# def sum_number(numbers):
#     nums = numbers.split(',')
#     return sum([int(num) for num in nums])











# Unittest

#1
# def convert_date_to_tuple(date):
#     day, month, year = date.split('-')
#     return (day, month, year)







#2
# def sum_of_list_elements(lst):
#     чreturn sum(int(num) for num in lst)






# 3
# def divide_sum_of_halves(lst):
#     half = len(lst) // 2
#     first_half = lst[:half]
#     second_half = lst[half:]
#
#     sum_first_half = sum(first_half)
#     sum_second_half = sum(second_half)
#
#     result = sum_first_half / sum_second_half
#     return result
