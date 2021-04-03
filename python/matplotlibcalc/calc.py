import matplotlib.pyplot as plt
import numpy as np

print("welcome to a graphing calculator coded in python")

degree = int(input("choose the degree of the polynomial: "))

coefficients = [0] * (degree + 1)

for i in range(degree + 1):
    coefficients[i] = int(input(f"enter {i + 1} coefficient: "))

coefficients = coefficients[::-1]

lowerx = int(input("enter lower bound of domain: "))
upperx = int(input("enter upper bound of domain: "))

lowery = int(input("enter lower bound of range: "))
uppery = int(input("enter upper bound of range: "))

x_list = np.arange(lowerx, upperx + 1, 0.1)
y_list = []

for x in x_list:
    y_sum = 0
    for i in range(1, len(coefficients) + 1):
        coefficient = coefficients[i - 1]
        if i == 1:
            y_sum += coefficient
        else:
            y_sum += coefficient * x ** (i - 1)

    y_list.append(y_sum)

plt.xlim([lowerx, upperx])
plt.ylim([lowery, uppery])

plt.grid()
plt.plot(x_list, y_list)
plt.show()

