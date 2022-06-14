class a:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show1(self):
        return f"name->{self.name} id ->{self.id}"

class b(a):
    def show2(self):
        return f"name->{self.name} id ->{self.id}"

if __name__ == '__main__':
    obj1 = b("mahadi", 21)
    print(obj1.show1())