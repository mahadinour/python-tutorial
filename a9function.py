def func1():
    print("hi")


func1()
print(func1())
print("--------------------")

def add(a, b):
    """"this is a add function and it is a docstrings"""
    r = a + b
    print("result ::::", r)
    func1()

a = int(input("a ="))
b = int(input("b ="))
add(a, b)

print(add(a, b))
print("-------")
print(add(a, b).__doc__)
print(add.__doc__)
print("========")


def list1(p):
    print(p)
p = [10 ,20, 30, 40]
list1(p)