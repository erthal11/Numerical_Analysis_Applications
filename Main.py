import sympy as sym

from mpmath import *

import time
start_time = time.time()

#Problem 1

def funca(x):
    return (2/x) - (1/pow(x,2))


def funcb(x):
    return (1/2)*(pow(x, 3) + 1)


#uses funca(x) and is unsuccessful because of division by 0
def fixedpointmethoda(p0, tolerance, nmax):
    print("Fixed point results: ")
    newp = p0
    i = 1

    while i < nmax:
        newp = funca(p0)
        if abs(newp - p0) > tolerance:
            p0 = newp
            print("At iteration", i, ", p = ", newp)
            i = i + 1
        else:
            print("Finally at iteration", i, ", p = ", newp)
            return
    newp

#uses funb(x)
def fixedpointmethodb(p0, tolerance, nmax):
    print("Fixed point results: ")
    newp = p0
    i = 1

    while i < nmax:
        newp = funcb(p0)
        if abs(newp - p0) > tolerance:
            p0 = newp
            print("At iteration", i, ", p = ", newp)
            i = i + 1
        else:
            print("Finally at iteration", i, ", p = ", newp)
            return
    newp

#The fixed point method using funca is unsuccessful, but funcb works so that one is appropriate
#fixedpointmethoda(0.5, 0.01, 100)
fixedpointmethodb(0.5, 0.01, 100)
print()




#Problem 3

e = mp.e

def myfunction(x):

    return pow(x, 3) + pow(x, 2) + 2*x
    # return pow(e, x) - x - 1


def bisectionmethod(a, b, tolerance, nmax):
    print("Bisection method results:")
    i = 1

    if myfunction(a) == 0:
        print("At iteration ", i, ", p = ", a)
        return

    elif myfunction(b) == 0:
        print("At iteration ", i, ", p = ", b)
        return

    else:

        while i < nmax:
            p = (a + b) / 2
            if abs(myfunction(p)) < tolerance:
                print("Finally at iteration", i, ", p = ", p)
                return
            else:
                if myfunction(a) * myfunction(p) < 0:
                    b = p
                    print("at iteration: ", i, ", p = ", p)
                    i = i+1
                else:
                    a = p
                    print("at iteration: ", i, ", p = ", p)
                    i = i + 1


def newtonsmethod(p0, tolerance, nmax):
    print("Newton method results:")
    i = 0
    p = p0
    x = sym.Symbol('x')
    fdiv = sym.diff(myfunction(x))
    fdiv = sym.lambdify(x, fdiv)
    while i <= nmax:
        newp = p - ((myfunction(p)) / (fdiv(p)))
        if abs(newp - p) <= tolerance:
            print("Finally at iteration", i, ", p = ", newp)
            return
        else:
            p = newp
            print("At iteration", i, ", p = ", newp)
            i = i + 1
    return "Method failed at newp = ", newp



def secantmethod (p0, p1, tolerance, nmax):
    print("Secant method results:")
    newp = p1
    i = 1
    while i < nmax:
            newp = p1 - (((myfunction(p1)) * (p1 - p0)) / ((myfunction(p1)) - myfunction(p0)))
            if abs(newp - p1) > tolerance:
                p0 = p1
                p1 = newp
                print("At iteration", i, ", p = ", newp)
                i = i+1
            else:
                print("Finally at iteration", i, ", p = ", newp)
                return

    return newp

bisectionmethod(-7,1, pow(10, -4), 300)
print()
newtonsmethod(1, pow(10, -4), 300)
print()
secantmethod(-1, 1, pow(10, -4), 300)

print()
print("time elapsed: {:.2f}s".format(time.time() - start_time))
