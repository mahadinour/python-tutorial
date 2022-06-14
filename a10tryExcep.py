try:
    n1 = int(input())
    n2 = int(input())
except Exception as  e:
    print(e)

try:
    print("sum of num ", n1 + n2)
except Exception as e:
    print(e)

print("------rip------")