#import
import numpy as np

#function
def F(x):
    return ((x ** 2) - np.cos(x))

def f(x):
    return ((2 * x) + np.sin(x))

#init
x = 1
counter = 1

#find root
while True:
    print(f"{counter:2d} : x = {x:.6e} , f(x) = {abs(F(x)):.6e}")
    ##print(str(x)+"hh"+str(F(x)))

    if (abs(F(x)) > 1e-15):
        x = (((-(F(x))) + (f(x) * x)) / f(x))
        counter += 1
    else:
        break