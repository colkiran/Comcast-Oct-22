
def outerFun(gname):            # local variable

    def innerFun():
        nonlocal gname          # only local variable can be converted into non
                                # local variables
        gname= "Steeve"
        gname= f"Mr.{gname}"
        print(f"Hello {gname}")
        print("hello world")

    innerFun()
    print(f"After :{gname}")

outerFun("Micheal")
