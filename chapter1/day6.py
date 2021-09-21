###1.6.1
#E.g 1
def sum_naturals(n)
    total, k = 0,1
    while k<=n:
        tpta;, k = total + k, k+1
    return total


sum_naturals(100)
"""5050"""

#E.g 2
def sum_cubes(n):
    total, k = 0,1
    while k<=n:
        total, k = total + k*k*k, k+1
    return total

sum_cubes(100)
"""
25502500
"""

#E.g 3
def pi_sum(n):
    total, l = 0,1
    while k<=n:
        total, k = total +8/ ((4*k-3) * (4*k-1)),k + 1
    return total

pi_sum(100)
"""
3.1365926848388144
"""

#Combination example
def summation(n, term):
    total, k = 0,1
    while k <=n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n,cube)

result = sum_cubes(3)


#Identity combination example
def summation(n,term):
    total, k = 0, 1
    while k<=n:
        total, k = total + term(k), k + 1
    return total

def identity(x):
    return x

def sum_naturals(n):
    return summation(n, identity)

sum_naturals(10)
" 55 "

summation(10, square)
"385"

#Pi example
def pi_term(x)
    return 8/ ((4*x-3) * (4*x-1))

def pi_sum(n):
    return summation(n, pi_term)

pi_sum(1e6)
"3.141592153589902"

###1.6.2

#Golden Ratio
def improve(update, close, guess=1):
    while note close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

improve(golden_update, square_close_to_successor)
"1.6180339887498951"

#Evaluation example
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

#Improve
def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

#Approx_eq
def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

#Improve
phi = improve(golden_update, square_close_to_successor)

#Maths Example

from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

improve_test()



###1.6.3

#2 arguments
def average(x,y):
    return (x+y)/2

def sqrt_update(x,a):
    return average(x,a/x)

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)



#sqrt
def average(x, y):
    return (x + y)/ 2

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

#F2
def sqrt(a):
    #F3
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x,a)
    return improve(sqrt_update, sqrt_close)


result = sqrt(256)




###1.6.4

#Skeleton
def compose1(f, g):
    def h(x):
        return f(g(x))
    return  h

#Example
def square(x):
    return x * x

def successor(x):
    return x + 1

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

 def f(x):
     """"Never called."""
    return -x


square_succesor = compose1(square, successor)
result = square_succesor(12)

###1.6.5

#Newton_update

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

#find_zero
def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)



#Square_root_Newton
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

>> square_root_newton(64)
8.0

def power(x, n):
    """Return x * x * x *.......* x for x repeated n times"""
    product, k = 1,0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)

>>> nth_root_of_a(2, 64)
8.0

>>> nth_root_of_a(3, 64)
4.0

>>> nth_root_of_a(6, 64)
2.0





###1.6.6
from math import pow
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h
curried_pow(2)



def map_to_range( start, end, f):
    while start < end:
        print(f(start))
        start = start + 1


def curry2(f):
    """ Retrun a curreid version of the given two-argument function."""

    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g


def uncurry2(g):
    """Return a two-argument version of the given curred function."""

    def f(x, y):
        return g(x)(y)

    return f

>>> pow_curried = curry2(pow)
>>> pow_curried(2)(5)
32



>>> uncurry2(pow_curried)(2, 5)
32



###1.6.7
def compose(f, g)
    return lambda x: f(g(x))

#Example 1
>>>s = lambda x: x * x
s
<function <lambda> at 0xf3f490>
>>> s(12)


#worked Example
def compose1(f, g)
    return lambda x: f(g(x))

f = compose1(lambda x: x * x,
             lambda y: y + 1)
result = f(12)

###1.6.9

def trace(fn)
    def wrapped(x):
        print('-> ', fn, '(', x, ')' )























