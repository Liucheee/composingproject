# 1.3#

def square(x):
    return mul(x, x)


print(square(21))
print(square(add(2, 5)))
print(square(square(3)))


def sum_squares(x, y):
    return add(square(x), square(y))


def sum_squares(x, y):
    return add(square(x), square(y))


###1.3.1###

from operator import mul


def square(x):
    # func / function name / formal parameters
    return mul(x, x)


# This example of a function square is defined and


f = max
max = 3
# binding 3 to max
result = f(2, 3, 4)
max(1, 2)
# causes error becuase max has already been bound to  the number 3.
# As a result cannot be used as a function #


###1.3.2###

# frame 1 is Day3.py
# frame 2 is big enviroment
# frame 3 is the inside the square
from operator import mul


def square(x):
    # frame 2

    return mul(x, x)


square(-2)
print("hello")

###1.3.2###
# frame 1 is Day3.py
# frame 2 is big environment
# frame 3 is the local environment inside the square function
# frame 4 is the local environment inside the sum_square function


from operator import add, mul


def square(x):
    return mul(x, x)

def sum_squares(x, y):
    return add(square(x), square(y))


result = sum_squares(5, 12)
