#import
import matplotlib.pyplot as plt
import numpy as np

#config
startT = 0
endT = 20
num = 10000
k = 1
m = 1
a = 10
bA = (4*k*m)**0.5 - 1.5
bB = (4*k*m)**0.5
bC = (4*k*m)**0.5 + 1.5

#data
t = []
xA = []
xB = []
xC = []

for i in range(0, num+1):
    t.append(float((((endT-startT) / (num)) * i)))
    xA.append(np.exp(-bA*t[i]/(2*m)) * (a*np.cos((t[i]/2)*(((4*k)/m)-((bA**2)/(m**2)))**0.5)))
    xB.append(np.exp(-bB*t[i]/(2*m)) * (a*np.cos((t[i]/2)*(((4*k)/m)-((bB**2)/(m**2)))**0.5)))
    xC.append(np.exp(-bC*t[i]/(2*m)) * (a*np.cos((t[i]/2)*(((4*k)/m)-((bC**2)/(m**2)))**0.5)))

#draw
plt.grid(axis = "both")
plt.ylabel("Displacement, x")
plt.xlabel("Time, t")
plt.xlim(0, 20)
plt.ylim(-12, 12)
plt.box(False)
plt.grid(False)
ax = plt.gca()
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xticks([])
ax.set_xticklabels([]) 
ax.xaxis.set_label_coords(0.95, 0.45)

plt.plot(t, xA ,color="blue", label="(a)")
plt.plot(t, xB, color="green", label="(b)")
plt.plot(t, xC, color="red", label="(c)")
plt.legend()
plt.show()

#Copyright © 2025 AbramSoft. All rights reserved.