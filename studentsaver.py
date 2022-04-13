
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
    #TODO: Save on data.txt

def readStudent():
    #TODO: Read Student
    print('')
def updateStudent():
    #TODO: Update Student
    print('')
def deleteStudent():
    #TODO: Delete Student
    print(' ')


while True:
    user_input = input("Choose: Create, Read, Update, Delete, Exit\n")
    if user_input == 'Create':
        createStudent()
    elif user_input == 'Read':
        readStudent()
    elif user_input == 'Exit':
        break
    else :
        print("Invalid command, please try again")

