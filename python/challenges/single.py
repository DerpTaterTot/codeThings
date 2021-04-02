def single(lst):
    answer = lst[0]
    for element in range(1, len(lst)):
        answer ^= lst[element]

    return answer


lst = [4,1,2,1,2]
print(single(lst))


