def curried_pow(x):
    def h():
        print("yes")

    return h


curried_pow(2)
curried_pow(27)()


# fucntion that adds 5 values curried

def addition(a, b, c, d, e) -> int:
    return sum(a + b + c + d + e)


addition(1, 2, 3, 4, 5)


#Curried function



