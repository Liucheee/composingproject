



###1.5.1


def square(x):
    mul(x, x) # Watch out! This call doesn't return a value.

# The body has a expression. The function nul is called but the result isn't stored
# For this to be valid it would require a assignment statement.Originally, we stated that the body of a user-defined function consisted only of a return statement with a single return expression. In fact, functions can define a sequence of operations that extends beyond a single expression.
#
# Whenever a user-defined function is applied, the sequence of clauses in the suite of its definition is executed in a local environment — an environment starting with a local frame created by calling that function. A return statement redirects control: the process of function application terminates whenever the first return statement is executed, and the value of the return expression is the returned value of the function being applied.
#
# Assignment statements can appear within a function body. For instance, this function returns the absolute difference between two quantities as a percentage of the first, using a two-step calculation:

def square(x):
    return mul(x, x)

# This example returns the null function value

def print_square(x):
    print(square(x))

# Sometimes it makes sense for non-pure functions


###1.5.3

def percent_difference(x, y):
    difference = abs(x-y)
    return 100 * difference / x
result = percent_difference(40, 50)


###1.5.4

def absolute_value(x):
"""Compute abs(x)."""
if x > 0:
    return x
elif x == 0:
    return 0
else:
    return -x

result = absolute_value(-2)

###1.5.5

def fub(n):
    """Compute the nth fibonacci number, for n>=2."""""
    pred,curr = 0,1 #first 2 values of the sequence
    k = 2           #the current count
    while k<n:
        pred,curr = curr,pred+curr
        k= k + 1
    return curr
result = fib(8)

###1.5.6
assert fib(8) == 13, 'The 8th fibonacci number should be 13'

def fib_test():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'


def sum_naturals(n):
    """Return the sum of the first n natural numbers

    >>>sum_naturals(10)
    55
    >>>sum_naturals(100)
    5050
    """
    total, k = 0,1
    while k <=n:
        total, k=total + k, k+1
    return total

from doctest import run_docstring_examples
run_docstring_examples(sum_naturals,globals(), true)

"""
Finding tests in NoName
Trying:
    sum_naturals(10)
expecting:
    55
ok 
Trying:
    sum_naturals(100)
Expecting:
    5050
ok 
"""

















