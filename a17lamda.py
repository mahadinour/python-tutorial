#lamda is one liner function
def add(x,y):
    return x+y
print(add(10, 20))

add1 = lambda a, b :print(a+b)
add1(10, 20)
print(add1(10, 20))
# lambda variable : function
min = lambda p, q: p+q
print(min(10, 40))


def a_first(a):
    return a[1]
a = [[1, 14], [5, 6], [8, 23]]
print(a)
a.sort(key=a_first)
print(a)