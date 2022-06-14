class Employee:
    def __init__(self, fname,  lname, salary):#constractor
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def Employee(self,name):
        pass


    pass # pass is a key word means nothing

#mahadi = Employee()#obj creat
#hassan = Employee()#obj creat

#mahadi.fname = "mahadi"
#mahadi.lname = "mounsi"
#mahadi.sarary = "400"

#hassan.fname = "hassan"
#hassan.lname = "rouf"
#hassan.sarary = "300"

#print(mahadi.lname)

nour = Employee("nour", "rahman", "5000")
print(nour.fname, nour.lname, nour.salary)