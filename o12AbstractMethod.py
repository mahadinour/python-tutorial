from abc import ABCMeta, abstractmethod

class a(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        return 0


class b(a):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def show(self):
        return f"rectangle -> {self.length * self.width}"

    def show(self):
        return f"cube -> {self.length * self.width * self.height}"

if __name__ == '__main__':
    print("hi")
    obj = b(10, 12, 14)
    print(obj.show())