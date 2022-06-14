class A:
    def show1(self):
        print("this is A ")


class B(A):
    def show2(self):
        print("this is B")
        super().show1()


class C(A):
    def show3(self):
        print("this is C")
        super().show1()


class D(B, C):
    def show4(self):
        print("this is D")
        super().show1()
        super().show2()
        super().show3()


if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    d = D()

    d.show4()


