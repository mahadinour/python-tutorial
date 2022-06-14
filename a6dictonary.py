d1 = {}
print(type(d1))
d2 = {"mahadi": "fish", "hassan ": "rice", "nour": "meat", "evan": {"b": "bread", "l": "rice", "d": "none"}}
print(d2)
print(d2["mahadi"])
print("dic in dic ----------------")
print(d2["evan"])
print(d2["evan"]["b"])

print("dic input ----------")
d2["miraf"] = "Gems"
print(d2)

d2["monifa"] = "milk"
print(d2)

del d2["evan"]
print(d2)

print("method----------")
print(d2.get("mahadi"))

d2.update({"mifta": "choclet"})
print(d2)
print(d2.get("mifta"))

print(d2.keys())
print(d2.items())