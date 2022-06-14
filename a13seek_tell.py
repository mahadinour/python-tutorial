f = open("a12.txt")

print(f.tell()) #tell where ur file pointer
print(f.readline())
print(f.tell())
print()
print("_______________")
p = open("a12.txt")

print(p.readline())
p.seek(10)