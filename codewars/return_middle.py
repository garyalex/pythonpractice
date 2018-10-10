def get_middle(s):
    if len(s) % 2 == 0:
        return s[int(len(s) / 2) - 1:int(len(s) / 2) + 1]
    else:
        return s[int(len(s) / 2)]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))
