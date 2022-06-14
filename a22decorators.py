def func1():
    print("subscrib")
func2 = func1

del func1
func2()