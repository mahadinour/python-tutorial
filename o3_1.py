class student :
    def __init__(self, Sname, Sage, Srole):
        self.name = Sname
        self.age = Sage
        self.role = Srole

    def show1(self):
        return f"name ->{student.name}\nage ->{student.age}\nrole ->{student.role}"

student = student("mic", 45, "hui")

stu = student("uiu", 45, "ji")