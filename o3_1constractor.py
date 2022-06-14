class student:
    def __init__(self, name, id, sec):
        self.n = name
        self.i = id
        self.s = sec
    def show(self):
        print(self.s, self.i, self.n)


if __name__ == '__main__':
    name = "mahadi"
    id = 21
    sec = 'a'
    obj = student(name, id, sec)
    obj.show()