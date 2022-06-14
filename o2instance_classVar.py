class employee:
    fname = "hassan"#class var


mahadi = employee()

mahadi.name = "mahadi"#instance var
print(mahadi.name)
print(mahadi.fname)

employee.fname = "nour1"
mahadi.fname = "nour2"
print(mahadi.name)
print(mahadi.fname)