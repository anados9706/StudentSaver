class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

def createStudent():
    name = input("Please enter Name")
    id = input("Please enter student id")
    gpa = input("Please enter GPA")
    new_student = Student(name,id,gpa)
    with open("data.txt", "a+") as data:
        data.write(id + "\n")
        data.write(name + "\n")
        data.write(gpa + "\n")


def readStudent():
    #TODO: ReadCreate  Student
    print('')
def updateStudent():
    #TODO: Update Student
    print('')

def deleteStudent():               #PORTER
    f = open("data.txt", "r+")
    f.seek(0)
    f.truncate()
    print("Data successfully deleted!")

while True:
    user_input = input("Choose: Create, Read, Update, Delete, Exit\n")
    if user_input == 'Create':
        createStudent()
    elif user_input == 'Read':
        readStudent()
    elif user_input == "Delete":
        deleteStudent()
    elif user_input == 'Exit':
        break
    else :
        print("Invalid command, please try again")