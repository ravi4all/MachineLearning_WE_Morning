students = []
student_record = {}

def addStudent():
    s_id = int(input("Enter student id : "))
    s_name = input("Enter student name : ")
    s_cgpa = float(input("Enter student cgpa"))

    # student_record["id"] = s_id
    # student_record["name"] = s_name
    # student_record["CGPA"] = s_cgpa

    student_record = {"id":s_id,"name":s_name,"cgpa":s_cgpa}

    students.append(student_record)

def readStudent():
    for s in students:
        print(s)


def updateStudent():
    pass


def deleteStudent():
    pass


def sortStudent():
    newlist = sorted(students, key=lambda k: k['id'])
    print("Sorted List")
    for n in newlist:
        print(n)

def searchStudent():
    pass

def errHandler():
    print("Wrong Choice....Enter Again")