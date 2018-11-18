# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
A program that prints the "Hello, World!" message.
"""

# A welcome message
print("Hello, World!")

x = input("Print input a number:")
print("The value of x is ", x)


x = input("x: ")
y = input("y: ")
print(x, "+", y, "=", x+y)


x = int(input("Input an integer:"))
y = float(input("Input a float:"))
print("x = ", x)
print("y = ", y)
print("x+y = ", x+y)
z = 'This is a string: "' + str(x+y) + '"'
print(z)

a = 10
b = 0.1
print("a =", a, "  b =", b, "  ->  ", "a + b - a =", a + b - a, "!=", b, "= b")
a = 10**7
b = 10**(-7)
print("a =", a, "  b =", b, "  ->  ", "a + b - a =", a + b - a, "!=", b, "= b")
a = 10**11
b = 10**(-11)
print("a =", a, "  b =", b, "  ->  ", "a + b - a =", a + b - a, "!=", b, "= b")


x = 474953
y = 1 / x
print(x * y)



def fib1(n):
    f0 = 0
    f1 = 1
    while n > 1:
        (f0, f1) = (f1, f0 + f1)
        n -= 1
    return f1

def fib2(n):
    sqrt5 = 5 ** .5
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return int((phi**n - psi**n) / sqrt5)

n = int(input("Type n (try to go for 73 or more): "))
fib1n = fib1(n)
fib2n = fib2(n)
print("|fib1(n) - fib2(n)| = |" + str(fib1n), "-", str(fib2n) + "| =", abs(fib1n - fib2n))

s = 0
for _ in range(1000):
    s += 0.1
print(s)
s = 0
for _ in range(10000):
    s += 0.1
print(s)
s = 0
for _ in range(10000000):
    last = s
    s += 0.1
print(s)



from math import pi
x = 15 * pi
# Create the list of series elements
elts = [ ]
f = 1
for k in range(1, 150, 2):
    elts.append(x**k / f)
    f *= -(k+1) * (k+2)
# Sum elements in the original order
sin1 = 0
for el in elts:
    sin1 += el
print("sin1 =", sin1)
# Sum elements in the reversed order
sin2 = 0
for el in reversed(elts):
    sin2 += el
print("sin2 =", sin2)
# Sum elements from the middle one to the ones on the edges
cnt = len(elts)
mid = cnt // 2
sin3 = 0
for i in range(mid + 1):
    if mid + i < cnt:
        sin3 += elts[mid + i]
    if i:
        sin3 += elts[mid - i]
print("sin3 =", sin3)
# Sum elements from the ones on the edge to the middle one
sin4 = 0
for i in reversed(range(mid + 1)):
    if mid + i < cnt:
        sin4 += elts[mid + i]
    if i:
        sin4 += elts[mid - i]
print("sin4 =", sin4)
print("|sin1 - sin4| =", abs(sin1 - sin4))
print("the first element:", elts[0])
print("the last element:", elts[-1])

#%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(elts)
plt.show()


from math import sqrt
x = float(input("x = "))
n = int(input("n = "))
t = x
for _ in range(n):
    t = sqrt(t)
for _ in range(n):
    t *= t
print("g(f(" + str(x) + ", " + str(n) + "), " + str(n) + ") =", t)
t = x
for _ in range(n):
    t *= t
for _ in range(n):
    t = sqrt(t)
print("f(g(" + str(x) + ", " + str(n) + "), " + str(n) + ") =", t)
