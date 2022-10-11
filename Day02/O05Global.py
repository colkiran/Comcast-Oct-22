
glbX = 100

def fun(a):                 # local variable
    global glbX
    print(f"a :{a}")
    glbX = 500
    print(f"Inside :{glbX}")
    b = "Hello"
    print(f"b :{b}")

print(f"before  :{glbX}")

fun(10)

print(f"After :{glbX}")
