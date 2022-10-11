

def outerFun(fnc):

    def helperFun(arg):
        print("logging into the server.....")
        fnc(arg)
        print("loggig out of the server......")
        print("-" * 40)

    return helperFun

@outerFun                   # deposit = outerFun(deposit)
def deposit(amt):
    print(f"{amt} credited into the account successfully....")


@outerFun
def withdraw(amt):
    print(f"{amt} debitted from the account successfully.....")

deposit(10000)
withdraw(2500)
