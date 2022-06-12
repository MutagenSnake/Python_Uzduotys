from functools import reduce
from statistics import mean, median

number_range = [item for item in range(0,51)]
number_multiplied = [print(item*10) for item in number_range]
numbers_dividable = [print(item) for item in number_range if item % 7 ==0]
numbers_squared = [print(item*item) for item in number_range]
numbers_squared_list = [item*item for item in number_range]
sum_of_square = reduce(lambda x, y: x + y, numbers_squared_list)
print(sum_of_square)
print(min(numbers_squared_list))
print(max(numbers_squared_list))
print(mean(numbers_squared_list))
print(median(numbers_squared_list))
numbers_squared_list.sort(reverse=True)
print(numbers_squared_list)