class student :
    lives = 40
    def __init__(self, Sname, Sage, Srole):
        self.name = Sname
        self.age = Sage
        self.role = Srole

    def show1(self):
        return f"name ->{st.name}\nage ->{st.age}\nrole ->{st.role}\nlives ->{st.lives}"

st= student("mic", 45, "hui")

st.lives = 50
print(st.lives)





