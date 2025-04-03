#import
import matplotlib.pyplot as plt
import numpy as np

#function
def f(x):
    y = 100 / (100 + (x - 1 / 2 * np.pi) ** 8) * (2 - np.sin(7 * x) - 1 / 2 * np.cos(30 * x))
    return y

#init
r=[]
theta=[]

#generate theta
i = - np.pi / 2

while (i <= 3 * np.pi / 2):
    theta.append(i)
    i += 2 * np.pi / 1000

#generate r
for i in theta:
    r.append(f(i))

#show plot
plt.figure()
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, color='green', linewidth=1)
ax.fill(theta, r, color='y', alpha=1)
ax.set_title("graph of 100/(100+(x-1/2*pi)**8)*(2-sin(7*x)-1/2*cos(30*x))", color='red')
plt.show()

#Copyright © 2025 AbramSoft. All rights reserved.