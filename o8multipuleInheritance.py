class a:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_a(self):
        return f"name ->{self.name} id -> {self.id}"



class b:
    def __init__(self, tool, lan):
        self.tool = tool
        self.lan = lan
    def show_b(self):
        return f"tool->{self.tool}language->{self.lan}"


class c(a, b):
    var = 2
    def show_c(self):
        return f"name ->{self.name}  id ->{self.id}  tool -> {self.tool} language -> {self.lan}"


if __name__ == '__main__':
    obj_c = c()
