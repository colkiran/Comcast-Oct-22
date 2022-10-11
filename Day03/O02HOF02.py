
def callMe():
    print("Apples from Ooty.....")

def fun(fnc):
    print("Hi......")
    fnc()
    print("hello......")
    print("-" * 40)

    def defineMe():
        print("Oranges from kanpur.....")

    return defineMe

def funCallBack(fnc):
    print("India is great......")
    fnc()
    print("Mera Bharath mahan.......")



funCallBack(fun(callMe))


