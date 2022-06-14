m = 10#global variable
o = 20

def function(n):
    m = 5#iocal variabla ,find first local and then find global
    print(n, "= this is n ")
    print(m)
    #o = o + 10 cant be possibal
    print(o)


function("N")
print(m)
print("----------------")


x = 60
def out( ):
    x = 20
    def into():
        global x
        x = 30
    print( "before calling in ", x)
    into()
    print("after calling in", x)

out()
print(x)