students = []

def addStudent():
    counter = 0
    s_id = int(input("Enter id of Student : "))
    name = input("Enter name of Student : ")
    cgpa = float(input("Enter CGPA of Student : "))

    students.append([s_id,name,cgpa])
    for s in students:
        counter += 1
        print(counter,s)

def readStudent():
    for s in students:
        print(s)


def updateStudent():
    to_update = int(input("Enter student id : "))
    current_student = students[to_update-1]
    print("You want to update record of :",current_student)

    to_update_name = input("Enter updated name : ")
    current_student[1] = to_update_name


def deleteStudent():
    to_delete = int(input("Enter student id : "))
    del(students[to_delete-1])


def sortStudent():
    to_sort = input("Press A to Sort in Ascending or D to Sort in Descending : ")
    if to_sort == "A":
        print(sorted(students))
        # for s in sorted_list:
        #     print(s)
    else:
        print(sorted(students,reverse=True))
        # for s in students:
        #     print(s)

def searchStudent():
    pass

def errHandler():
    print("Wrong Choice....Enter Again")

mainLoop = False

while True:
    
    print("""
    1. Add Student
    2. Read Student
    3. Update Student
    4. Delete Student
    5. Sort Students
    6. Search Student
    7. Press q to exit
    """)

    to_select = {
        "1" : addStudent,
        "2" : readStudent,
        "3" : updateStudent,
        "4" : deleteStudent,
        "5" : sortStudent,
        "6" : searchStudent,
        "q" : exit
    }

    user_choice = input("Enter your choice : ")

    to_select.get(user_choice,errHandler)()
