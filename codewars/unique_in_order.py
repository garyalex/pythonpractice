def unique_in_order(my_string):
    my_list = list(my_string)
    prev_char = ""
    ret_list = []
    for char in my_list:
        if char != prev_char:
            ret_list.append(char)
        prev_char = char
    return ret_list


print(unique_in_order('AAAABBBCCDAABBB'))
