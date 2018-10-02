def friend(x):
    return [friend for friend in x if len(friend) == 4]


print(friend(["Ryan", "Kieran", "Mark", ]))
