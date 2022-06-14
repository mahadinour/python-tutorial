class a:
    def __init__(self, n, i, l):
        self.name = n
        self.id = i
        self.lan = l

    def show(self):
        return f"{self.name}->{self.id}->{self.lan}"

class b(a):
    def show1(self):
        return f"{self.id}->{self.name}-> {self.lan}"


#obj1 = a("name", 23)
obj2 = b("name1", 24, ["python", 'c'])
print(obj2.show1())
print(obj2.show())


