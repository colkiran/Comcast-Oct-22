
from abc import ABC, abstractmethod

class Employee(ABC):

    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Managers job......")

class Developer(Employee):

    def doJob(self):
        print("Developer job.......")


Mike = Manager()
Dave = Developer()

def bankJob(emp):
    print("Bank job started.....")
    emp.doJob()
    print("Bank job ended......")
    print("-" * 40)


bankJob(Mike)
bankJob(Dave)
