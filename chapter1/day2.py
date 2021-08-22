#1.2.2#
print("1.2.2")
print(max(7.5,9.5))

print(pow(100,2))

print(pow(2,100))

print(max(1,-2,3,-4))

print(max(min(1, -2), min(pow(3, 5), -4)))

#1.2.3#
print("1.2.3")

from math import sqrt
print(sqrt(256))

from operator import add, sub, mul
print(add(14, 28))

print(sub(100, mul(7, add(8, 4))))


#1.2.4#
print("1.2.4")
from math import pi
radius = 10


area, circumference = pi * radius*radius, 2 * pi * radius
print("area = ", area)
print("circumference = ", circumference)

radius = 11
print("area =", area)
area = pi*radius*radius
print("new area = ", area)


x,y = 3,4.5
y,x = x,y

print(x)
print(y)

#1.2.6#
print("1.2.6")

two = print(2)
print(two)


