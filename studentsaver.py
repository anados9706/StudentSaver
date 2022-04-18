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
    id = input("Please enter student id ")
    with open("data.txt", "r") as myfile:
        data = myfile.readlines()
    with open("data.txt", "w") as myfile:
        deleted = False
        i=0
        while i < len(data):
            if data[i].replace("\n", "")!=id:
                myfile.write(data[i])
                myfile.write(data[i+1])
                myfile.write(data[i+2])
            else:
                deleted = True
                print(id + " successfully deleted!")
            i+=3
        if not deleted:
            print("Nothing to delete")

    
    
    

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