
def outerFun(fnc):

    def helperFun(a, b):
        if b > a:
            a, b = b, a
        print(fnc(a, b))
        print("-" * 40)

    return helperFun

@outerFun
def diff(x, y):
    print(f"difference of {x}, {y}")
    return x - y

diff(30, 15)
diff(15, 30)
diff(20, 80)
diff(100, 250)