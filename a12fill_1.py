def getdate():
    import datetime
    return datetime.datetime.now()

p = open("bebe2.txt", "r+")
p.write(str(getdate()))
print(p.read())
print("readable ", p.readable())
print("writeable ", p.writable())

