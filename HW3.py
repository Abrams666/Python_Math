#import
import matplotlib.pyplot as plt
import numpy as np

#config
a = 1
b = 3.2
n = 10001

plt.title("f(x) = ln(x)/x and computed derivative")
plt.grid(axis = "both")
plt.xlabel("x")
plt.ylabel("y")

#data
x = []
y1 = []
y2 = []

for i in range(1, n+1):
    x.append(float((((b-a) / (n-1)) * i) + 1))
    y1.append(float(np.log(x[i-1]) / x[i-1]))

y2 = np.gradient(y1, x)

#draw
plt.plot(x, y1 ,color="blue")
plt.plot(x, y2, color="green")
plt.show()

#Copyright © 2024 Abrams. All rights reserved.