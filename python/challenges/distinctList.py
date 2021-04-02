def distinct(lst):
    sameTotal = 0
    for x in range(len(lst)):
        for y in range(x + 1, len(lst)):
            if lst[x] == lst[y]:
                sameTotal += 1

    return len(lst) - sameTotal


print(distinct(['bcdef', 'abcdefg', 'bcde', 'bcdef']))