import matplotlib.pyplot as plt

print("welcome to a graphing calculator coded in python")

degree = int(input("choose the degree of the polynomial: "))

coefficients = [0] * (degree + 1)

for i in range(degree + 1):
    coefficients[i] = int(input(f"enter {i + 1} coefficient: "))

lowerx = int(input("enter lower bound of domain: "))
upperx = int(input("enter upper bound of domain: "))

lowery = int(input("enter lower bound of range: "))
uppery = int(input("enter upper bound of range: "))

plt.xlim([lowerx, upperx])
plt.ylim([lowery, uppery])

plt.show()