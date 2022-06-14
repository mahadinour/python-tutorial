#49
num = ["3", "34", "64"]
for i in range(len(num)):
    num[i] = int(num[i])
num[2] = num[2] + 1
print(num[2])

num1 = ["6", "9", "10"]
map(int, num1) #int will apply all the element
print(map(int, num1))
print(list(map(int, num1)))


def sq(a):
    return a*a



num2 = [2, 3, 4, 5, 6]


square = list(map(sq, num2))
print(square)

# lambda variable : function
# map(function , iterables)
num3 = [2, 3, 4, 5, 6]
square1 = list(map(lambda x: x*x, num2))
print(square1)


def squ(a):
    return a*a


def cube(a):
    return a*a*a


function = [squ, cube]
for i in range(5):
    val = list(map(lambda x:x(i), function))
    print(val)

print("filter ++++++++++++++++++++")

list1 = [1, 2, 3, 4, 5, 6, 7]


def is_greatter_5(num):
    return num >= 5


gr_then_5 = list(filter(is_greatter_5, list1))

print(gr_then_5)

print("reduce +++++++++++")

list2 = [1, 2, 3, 4, 5, 6, 7]
x = 0
for i in list2:
    x = x +i
print(x)

from functools import reduce

r  = reduce(lambda x,y: x+y, list2)

print(r)