

def add(x, y):
    print(f"adding {x}, {y}")
    return x + y

def sub(x, y):
    print(f"subtraction {x}, {y}")
    return x - y


def outerFun(fnc):

    def helperFun(*args):
        print("Logging into the service....")
        print(fnc(*args))                        # call back
        print("Logging out of the service.....")
        print("-" * 40)

    return helperFun

addlogger = outerFun(add)
sublogger = outerFun(sub)


addlogger(30, 180)
sublogger(180, 30)
