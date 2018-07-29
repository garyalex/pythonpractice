def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    return list(i for i in numbers if (i % 2 == 0 and i > 0))


nums = [1, 2, 4, -1, 11, 6, 0, 8]
print(filter_positive_even_numbers(nums))
