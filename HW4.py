#import
import matplotlib.pyplot as plt
import numpy as np

#function
def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1,n):
            n*=i

        return n

#init
x=[]
y=[]

#config chart
plt.title("Taylor polynomials with different orders for cos^2(x)")
plt.grid(axis = "both")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-2, 3)

#generrate x
i=-6.2

while (i<=6.2):
    x.append(i)
    i+=0.001

#generate y
for i in range(1,11):
    for j in range(len(x)):
        y_temp=0

        for k in range(1,i+1):
            y_temp+=((((-1)**(k))*((2*x[j])**(2*k)))/(2*(factorial(2*k))))

        y.append(1+y_temp)

    plt.plot(x, y, label="P"+ str(2*i))
    y=[]

for i in range(len(x)):
    y.append((np.cos(x[i]))**2)

plt.plot(x, y, label="cos^(x)")

#show chart
plt.legend(loc="upper right")
plt.show()

#Copyright © 2025 AbramSoft. All rights reserved.