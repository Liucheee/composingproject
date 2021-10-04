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










