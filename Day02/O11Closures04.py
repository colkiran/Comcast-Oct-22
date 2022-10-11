
def outerFun(greet):

    def innerFun(sep):

        def innermost(name):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)
        return innermost

    return innerFun

engGrt = outerFun("Welcome")
engTgr = engGrt('tiger')
engTgr("Sheroff")



"""
engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vanakam")

slengGrt = engGrt("----->")
sltmlGrt = tmlGrt("----->")

slengGrt("Mike")
sltmlGrt("Kumar")
"""