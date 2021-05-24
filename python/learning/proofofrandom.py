import numpy as np

count = [0, 0, 0, 0, 0]

accuracy = 100000

for _ in range(accuracy):
    a = np.random.randint(5)
    count[a] += 1

for i in range(len(count)):
    print(f"The percentage of {i}s is {count[i]/accuracy*100}%")