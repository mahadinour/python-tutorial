class a:
    def __init__(self):
        self.name = "mahadi"
        self.sec ='a'
    def show1(self):
        print(self.name, self.sec)


class b(a):
    def __init__(self):
        super().__init__()
        self.name = "nour"
        self.sec = 'b'


if __name__ == 'main':
    obj1 = a()
    obj2 = b()

    obj1.show1()
    print(obj2.name, obj2.sec)