list1 = [ "a", "b", "c", "d", "e", "f"]
print(list1[0], list1[5])

for i in list1:
    print(i)

list2 = [
    ["mahadi", 1],
    ["hassan", 2],
    ["nour", 3]
]
for i, name in list2:
    print(i, name)

dict1 = dict(list2)
print(dict1)

for i, name in dict1.items():
    print(i, "name list ", name)

for i in range(0, 10):
    print(i)
print("______________")
for j in range(10, -1, -1):
    print(j)
print("++++++++++++++++++++++++++++++")
a = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
print(len(a))
for j in range(10, -1, -1):
    print(a[j])
