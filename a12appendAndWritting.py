f = open("a12.txt", "w")

b = f.write(input("enter ur name "))

a = f.write("\n mahadi hassan nour ")
print("no of cher ", a)
print("no of cher ", b)


c = open("a12.txt", "r+")
print(c.read())
c.write("thank u     ")
f.close()