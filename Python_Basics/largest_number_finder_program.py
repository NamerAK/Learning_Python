def largest_numbers_finder(numbers_list, largest_numbers_range):
    numbers_list.sort()
    return numbers_list[-largest_numbers_range: ]


numbers = [1,2,9,4,8,3,5,7,6]

range_of_largest_numbers = 3

print(f'List before sorting: {numbers}\n')

largest_numbers = largest_numbers_finder(numbers, range_of_largest_numbers)

largest_numbers.sort(reverse=True)


print(f'List after sorting: {numbers}\n')

print(f'List of first {range_of_largest_numbers} numbers: {largest_numbers}')
