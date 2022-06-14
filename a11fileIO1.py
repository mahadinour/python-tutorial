f = open("a11fileIO2.txt", "rt")
cont = f.read()
print(cont)

cont = f.read(222222)
print("1", cont)

cont = f.read(333333)
print("2", cont)


for line in cont:
    print(line)


f.close()