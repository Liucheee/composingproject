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


#Curried 5 variable function

def multiple(a):
    def g(b):
        def h(c):
            def i(d):
                def j(e):
                    print(a, b, c, d, e)
                return j
            return i
        return h
    return g

multiple(1)(2)(3)(4)(5)



