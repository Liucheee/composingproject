###1.6.1

def sum_naturals(n)
    total, k = 0,1
    while k<=n:
        tpta;, k = total + k, k+1
    return total


sum_naturals(100)
"""5050"""

def sum_cubes(n):
    total, k = 0,1
    while k<=n:
        total, k = total + k*k*k, k+1
    return total

sum_cubes(100)
"""
25502500
"""

def pi_sum(n):
    total, l = 0,1
    while k<=n:
        total, k = total +8/ ((4*k-3) * (4*k-1)),k + 1
    return total

pi_sum(100)
"""
3.1365926848388144
"""






