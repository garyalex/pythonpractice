def reverse3(nums):
    newlist = []
    for i in nums:
        newlist.insert(0, i)
    return newlist


print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))