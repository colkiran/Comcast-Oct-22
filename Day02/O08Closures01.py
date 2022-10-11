
# closures
def outerFun(nm):
    gnm = f"Mr.{nm}"

    def innerFun():

        print("hello world")
        print(f"Greetings {gnm}")

    innerFun()


outerFun("Kevin")
