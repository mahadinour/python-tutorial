class teacher :
    sub = 3


class student:
    _gpa = 3.42

class stuff:
    __sallary = 5000
    def __show(self):
        print("slarry is private")

if __name__ == '__main__':
    tec = teacher()
    print(tec.sub)

    stu = student()
    print(stu._gpa)

    sff = stuff()
    print(sff._stuff__sallary)
    sff._stuff__show()