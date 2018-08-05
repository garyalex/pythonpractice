def split_array(array):
    list1 = []
    list2 = array

    while sum(list1) < sum(list2):
        list1.append(list2[0])
        del list2[0]
        if sum(list1) == sum(list2):
            return list1, list2

    return None


print(split_array([1, 1, 2, 3]))
