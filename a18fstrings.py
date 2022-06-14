import math

name = "mahadi"
num = 100
var = "this is %s %s" % (name, num)
print(var)
a = "this is {1} {0}"
var2 = a.format(name, num)
print(var2)

b = f"this is {name} {num} {math.cos(0)}"
print(b)