class employe:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    def mail(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    @property
    def Gmail(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"

    @Gmail.setter
    def Gmail(self, string):
        print("setting now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @Gmail.deleter
    def Gmail(self):
        self.fname = None
        self.lname = None

bangladeshi = employe("bangla" , "supporter")
mahadi = employe("mahadi", "nour")

print(bangladeshi.explain())
print(bangladeshi.email)
print(mahadi.email)

bangladeshi.fname = "US"
print(bangladeshi.email)
print(bangladeshi.mail())
print(bangladeshi.Gmail)
bangladeshi.Gmail = "this.that@gmail.com"
print(bangladeshi.Gmail)
del bangladeshi.Gmail
print(bangladeshi.Gmail)