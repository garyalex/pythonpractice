def pair_sum(array, total):
    if len(array) < 2:
        return print('Too small')

    seen = set()
    output = set

    for num in array:
        target = total - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target, num), max(target, num)))

    return output
