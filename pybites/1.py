def sum_numbers(numbers=None):
    if numbers == None:
        numbers = range(1, 101)

    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]

    return sum


print(sum_numbers([5, 6, 14, 11]))
print(sum_numbers())
