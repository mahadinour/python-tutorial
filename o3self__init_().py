class employee:
    fname = "hassan"

    def displsy(self):
        return f"name ->{mahadi.name}\nfname ->{mahadi.fname}\nage->{mahadi.age}"

mahadi = employee()

mahadi.fname = "nour"
mahadi.name = "mahadi"
mahadi.age = 30


mahadi.displsy()
print(mahadi.displsy())

print("++++++++++++++")

#s->agument variable
#name, age, role ->instance

"""CONSTRACTOR"""
class student:
    def __init__(self, Sname, Sage, Srole):
        self.name = Sname
        self.age = Sage
        self.role = Srole

    def show(self):
        return  f"name ->{st.name}\nage ->{st.age}\nrole ->{st.role}"

    def show1(self):
        print("hi")
        print(self.role)
        print(self.age)
        print(self.show())

n = input("name")
a = int(input("age "))
r = input("role")
st = student(n, a, r)
st.show()

print(st.show())

""" __self__"""
class SELF:
    pass

if __name__ == '__main__':
    obj = SELF()





