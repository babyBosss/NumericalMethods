import numpy as np

def f(v):
    x = v[0][0]
    y = v[1][0]
    return ((1-x)**2)+5*(y-x**2)**2

def grad(v):
    x = v[0][0]
    y = v[1][0]
    return np.array([[-20*x*(-(x*x)+y)+2*x-2], [-10*x*x+10*y]])

def hess(v):
    x = v[0][0]
    y = v[1][0]
    return np.array([[60*x*x-20*y+2, -20*x], [-20*x, 10]])

eps = 1e-12
v = np.array([[5], [5]])
i = 0
d = 1
print("  i            x                     y                     r")
while d > eps:
    earl = f(v)
    v = v - np.dot(np.linalg.inv(hess(v)), grad(v))
    d = abs(earl - f(v))
    print(i, "   ", v[0][0], "   ", v[1][0], "   ", d)
    i = i + 1


