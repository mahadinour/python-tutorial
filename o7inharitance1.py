class a:
    xxx = 10
    def show1(self):
        print("class a,show1")


class b(a):
    def show2(self):
        print("class b,show2")


obj = b()
obj.show2()
obj.show1()
obj.xxx
print(isinstance(a,b))