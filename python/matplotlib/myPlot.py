import matplotlib.pyplot as plt
import numpy as np
import math

lst = np.linspace(0, math.pi*2, 100)
x = [5 * math.cos(b) for b in lst]
y = [5 * math.sin(a) for a in lst]


plt.plot(x, y, 'rp', label='linear')

plt.axis('equal')
plt.legend()

plt.show()
plt.axis('equal')
plt.legend()
