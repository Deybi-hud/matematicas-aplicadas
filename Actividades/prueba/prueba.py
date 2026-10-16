import matplotlib.pyplot as ptl
import numpy as np
from scipy.optimize import fsolve

x1, x2 = 25664, 42561
y1, y2 = 1030, 1706

m = (y2-y1)/(x2-x1)
n = y1 - m * x1

def f(x):
    return 0.04*x+3.08

print(f"{f(25664):.0f}")

print(f"{m:.2f}\n")
print(f"{n}\n")


def a(t):
    return 0.36*t**2

def b(t):
    return 0.16*t**2+t+10


def intercer(x):
    return a(x)-b(x)

solucion = fsolve(intercer, 10)[0]
print(f"{round(solucion)}\n")

print(f"{a(10):.0f}\n")
print(f"{b(10):.0f}\n")


def i(x):
    return 60*x+3*x**2

def c(x):
    return 50*x+2400-4400

solucion = fsolve(c, 1)[0]
print(f"{round(solucion)}\n")
print(f"{i(40)}\n")


def t(n):
    return 2*(1.05)**n

print(f"{t(33):.1f}\n")

def s(t):
    return 1000*(1-np.exp(-0.3*t))-639 

solucion = fsolve(s, 1)[0]
print(f"{solucion:.1f}")

def s(t):
    return 1000*(1-np.exp(-0.3*t))

print(f"{s(3.4)}")

#A -
#B -
#C -
#D x