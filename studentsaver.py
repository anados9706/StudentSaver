class Student:
    def __init__(self, name, ID, GPA):
        self.name = name
        self.ID = ID
        self.GPA = GPA

def createStudent():
    name = input("Please enter Name")
    ID = input("Please enter student ID")
    GPA = input("Please enter GPA")
    new_student = Student(name,id,GPA)
    with open("data.txt", "a+") as data:
        data.write(name + "\n")
        data.write(id + "\n")
        data.write(gpa + "\n")

def readStudent():              #Marina
    ID = input("Please enter student ID ")
    myfile = open("data.txt", "r")
    contents = myfile.readlines()
    i=0
    while i < len(contents):
        if contents[i].replace("\n", "")==ID:
            print(contents[i])
            print(contents[i+1])
            print(contents[i+2])
        myfile.close()
        i+=3
  
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