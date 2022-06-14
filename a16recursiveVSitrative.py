def factorial_itrative(n):
    fac = 1
    for i in range(n):
        fac = fac *(i+1)
    return fac

print("factorial_itrative num1")
num1 = int(input("enter a number "))
print(factorial_itrative(num1))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

print (" factorial_recursive num2 ")
num2 = int(input("enter a number "))
print(factorial_recursive(num2))