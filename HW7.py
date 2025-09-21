#import
import matplotlib.pyplot as plt
import numpy as np

#config
a = 0
b = 20
n = 10000

plt.title("f(x) = 5+sqrt(x)*sin(x/pi) and computed derivative")
plt.grid(axis = "both")
plt.xlabel("X")
plt.ylabel("Y")
plt.xticks([0, 2.5, 5, 7.5,10,12.5,15,17.5, 20]) 
plt.yticks([0, 2, 4, 6])

#data
x = []
y1 = []
y2 = []

for i in range(0, n+1):
    x.append(float((((b-a) / (n)) * i)))
    y1.append(float(5+(np.sqrt(x[i])*np.sin(x[i]/np.pi))))

y2 = np.gradient(y1, x)

#draw
plt.plot(x, y1 ,color="blue")
plt.plot(x, y2, color="green")
plt.show()

#Copyright © 2025 AbramSoft. All rights reserved.