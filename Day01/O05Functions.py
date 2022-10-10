
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")

def greetgst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city is the default argument and gname is non default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event..... ")

greet()

print("-" * 40)
greetgst("Rahul")
greetgst("Sachin")

print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
# named Args
def admisn(name, dob, qlf, comp, contno, adr, city, gender):
    print(f"Name :{name}")
    print(f"DOB  :{dob}")
    print(f"Qlf  :{qlf}")
    print(f"Comp :{comp}")
    print(f"contno :{contno}")
    print(f"address :{adr}")
    print(f"city :{city}")
    print(f"gender :{gender}")


# *args => like a list
admisn('Jack', '12/05/1982', 'MBA', 'IBM', '334546734', 'indira nagar, 10th cross, 1st main', "Bangalore", 'Male')

print("-" * 40)
# **kwargs => like a dictionary
admisn(city="Mumbai", dob='09/03/1979', comp="Verizon", qlf="Btech", name='Joe',
       gender='Female', adr="Ashok nagar, 12th main", contno="34234234")

