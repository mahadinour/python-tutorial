class Student:
    lives = 40

    def __init__(self, Sname, Sage, Srole):
        self.name = Sname
        self.age = Sage
        self.role = Srole

    def show1(self):
        return f"name ->{st.name}\nage ->{st.age}\nrole ->{st.role}\nlives ->{st.lives}"


    @classmethod
    def from_srt(cls, string):
        prams = string.split("-")
        return cls(prams[0], prams[1], prams[2])


st= Student("mic", 45, "hui")


karan = Student.from_srt("karan-480-student")
print(karan.role)


