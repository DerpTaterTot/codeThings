import numpy as np
import matplotlib.pyplot as plt

N_points = 10000000
n_bins = 20

# Generate a normal distribution, center at x=0 and y=5
x = np.random.normal(loc=150, scale = 5, size=N_points)

plt.hist(x)
plt.show()
