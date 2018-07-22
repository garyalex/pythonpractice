def rotate_left3(nums):
    newarray = nums[1:]
    newarray.append(nums[0])
    print(newarray)

rotate_left3([1, 2, 3])
rotate_left3([5, 11, 9])
rotate_left3([7, 0, 0])