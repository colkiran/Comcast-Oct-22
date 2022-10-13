
# duck types
class Manager():

    def doJob(self):
        print("Managers job......")

class Developer():

    def doJob(self):
        print("Developer job.......")


Mike = Manager()
Dave = Developer()

def bankJob(emps):
    print("Bank job started.....")
    for emp in emps:
        emp.doJob()
    print("Bank job ended......")
    print("-" * 40)


bankJob([Mike, Dave])

