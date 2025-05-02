#import
import sympy as sy
from sympy import *

#init
init_printing()

x = sy.symbols('x')
y = sy.symbols('y')
f = x * sy.sin(y) * sy.cos(x)

#dxdy
fi = f

for i in range(3) :
    fi = sy.Integral(fi, x, y)
    sy.pprint(fi)
    fi = fi.doit()                        
    print("=")
    sy.pprint(fi)
    print()

#dydx
fi = f

for i in range(3) :
    fi = sy.Integral(fi, y, x)
    sy.pprint(fi)
    fi = fi.doit()                        
    print("=")
    sy.pprint(fi)
    print()

#Copyright © 2025 AbramSoft. All rights reserved.