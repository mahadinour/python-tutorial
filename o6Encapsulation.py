class encap:
    def __init__(self, name, roll, sec):
        self.name = name
        self.roll = roll
        self.sec = sec
    def set_name(self, val):
        self.name = val
    def get_name(self):
        return self.name


if __name__ == '__main__':
    obj = encap("mahadi", 21, 'c')
    obj.set_name("nour")
    print(obj.name)
    print(obj.get_name())

    obj1 = encap("mahadi", 21, 'c')
    print(obj1.name)