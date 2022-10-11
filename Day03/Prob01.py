

def outerFun(func1):
    def inner_fun(*args):
        func1(*args)
    return inner_fun

@outerFun
def fun():
    print(f"function fun1.......")

@outerFun
def fun1(x):
    print(f"function fun2.......{x}")

@outerFun
def fun2(x, y):
    print(f"function fun3.......{x} {y}")

@outerFun
def fun3(x, y, z):
    print(f"function fun4.......{x} {y} {z}")

@outerFun
def fun4(x, y, z, a):
    print(f"function fun5....... {x} {y} {z} {a}")


fun()
fun1(10)
fun2(10, 20)
fun3(100, 220, 503)
fun4(90, 80, 70, 60)

