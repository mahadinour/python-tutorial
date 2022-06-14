class a:
    def __init__(self, name, slarry, roll):
        self.name = name
        self.slarry = slarry
        self.roll = roll

    def __add__(self, other):
        return self.slarry + other.slarry

    def __truediv__(self, other):
        return self.slarry / other.slarry

    #def __str__(self):
    #    return f"name {self.name}   slarry {self.slarry}    roll {self.roll}"

if __name__ == 'main':
    x = a("mahadi" , 30000, "proggamer")
    y = a("nour", 40000, "swe")
    print(x + y)