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

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

phi = improve(golden_update, square_close_to_successor)

#Maths Example

from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, )















