#import
import matplotlib.pyplot as plt
import pylab
import numpy as np

#config
a = 1
b = 20
n = 10001

plt.title("f(x) and f'(x)")
plt.grid(axis = "both")
plt.xlabel("x")
plt.ylabel("y")

#data
x = []
y1 = []
y2 = []

for i in range(1, n+1):
    x.append(float((((b-a) / (n-1)) * i) + 1))
    y1.append(float(((2 * (((pylab.sin(x[i-1]))) + (pylab.cos((2 * x[i-1]))) + 3)) / (x[i-1] + 1)) ** 0.5))

y2 = np.gradient(y1, x)

#draw
plt.plot(x, y1 ,color="blue")
plt.plot(x, y2, color="green")
plt.show()