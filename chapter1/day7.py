###1.7
#Example 1
>>> 18117 % 10
7

>>> 18117 // 10
1811

#Example sum_digits
Def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = n //10, n % 10
        return sum_digits(all_but_last) + last


#Recursive using while statement
#iterative
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total,, k = total * k, k + 1
    return total

fact_iter(4)
24


#recursive
def fact(n)
    if n ==1:
        return 1
    else:
        return n * fact(n-1)
    
fact(4)


### 1.7.2




