
# varaible length args

def prodAll(*numbers):             # accept more than one arg in form of a tuple
    print(*numbers)             # unpack
    print(numbers)
    prod = 1
    for number in numbers:
        prod *= number

    return prod

print("The result is :", prodAll(1, 2, 3, 4, 5))

print("-" * 40)

def extractDetails(**details):      # takes more than one arg like a dictionary
    print(details)
    print("-" * 40)
    for k, v in details.items():
        print(k, "=>",  v)

extractDetails(name="Sachin", runs=140, oppn="West Indies", Venue="Sabina Park")

print("-" * 40)

def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmeticCalc(20, 8)
print(f"res :{res}")

# Python support recursive calls
# using recursive calls
    # write code to find the factorial of a number
    # write a code generate fibanocci series


def fact(n):
  return 1 if n<=1 else n * fact(n-1)

print(fact(5))

def fib(n):
  return n if n<=1 else fib(n-1) + fib(n-2)

# iter = int(input ( "Enter the number of iteration :"))
iter = 5
for i in range(0,iter+1):
    print(fib(i), end=" ")
print()

print("-" * 40)

def fun():
    "This is a doc string"
    # This is a comment
    print("hello world....")

fun()
print(fun.__doc__)

print("-" * 40)

def fun1(x, y):
    """
    funtion - fun1(x, y)

    function fun1 will take x and y as arguments
    if x and y are integers then the result would be the sum of x and y
    if x and y are strings then the result would be the concatenation of x and y
    if they are of two different datatypes then the result would be an error
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello", "world"))

print("-" * 40)
help(fun1)