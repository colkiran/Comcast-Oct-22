
# closure
def outerFun(nm):               # HOF - Higher Order Function
    gnm = f"Mr.{nm}"

    def innerFun():

        print("hello world")
        print(f"Greetings {gnm}")

    return innerFun


outerFun("Kevin")
print("-" * 40)

print(outerFun.__name__)
print(outerFun("abc").__name__)

print("-" * 40)
infun = outerFun("Slater")

print("After few lines of code")
infun()                         # calls the inner function

print("-" * 40)
outerFun("Peter")()             # calls the inner fun
