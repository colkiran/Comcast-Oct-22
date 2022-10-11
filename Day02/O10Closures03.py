
def outerFun(greet):

    def innerFun(name):

        print(greet, name)

    return innerFun

# simple curry

#curry
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")

# any dish
engGrt("Louis")
tmlGrt("Natraj")
