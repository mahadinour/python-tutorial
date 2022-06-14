
def printhar(string):
    return f"this is string {string}"
def add(num1 , num2):
    return num1 + num2 +5

print(__name__)

if __name__ == '__main__':# used to execute some code only if the file was run directly,
    print(printhar("harry"))
    o = add(4 , 6)
    print(o)
