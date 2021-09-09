def curried_pow(x):
    def h(y):
        return pow(x, y)
    return print

print(curried_pow(2))
curried_pow(2)(3)
