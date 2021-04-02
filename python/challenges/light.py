
file = open('/home/albertchen/works/pythonworks/challenges/newfile.txt', 'r')

dlist = []
d = {}
count = 1
for line in file:
    x = line.split(":")
    a = x[0]
    b = x[1]
    b = b[0:-1]

    d[a] = b

    if count == 4:
        dlist.append(d)
        count = 1

    count += 1

print(dlist)  
print(len(dlist))  