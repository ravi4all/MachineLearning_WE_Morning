import Student

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
        "1" : Student.addStudent,
        "2" : Student.readStudent,
        "3" : Student.updateStudent,
        "4" : Student.deleteStudent,
        "5" : Student.sortStudent,
        "6" : Student.searchStudent,
        "q" : exit
    }

    user_choice = input("Enter your choice : ")

    to_select.get(user_choice,Student.errHandler)()