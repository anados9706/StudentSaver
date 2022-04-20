class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

def createStudent():
    name = input("Please enter Name ")
    id = input("Please enter student ID ")
    gpa = input("Please enter GPA ")
    new_student = Student(name,id,gpa)
    with open("data.txt", "a+") as data:
        data.write(id + "\n")
        data.write(name + "\n")
        data.write(gpa + "\n")

def readStudent():              #Marina
    id = input("Please enter student ID ")
    myfile = open("data.txt", "r")
    contents = myfile.readlines()
    i=0
    while i < len(contents):
        if contents[i].replace("\n", "")==id:
            print(contents[i])
            print(contents[i+1])
            print(contents[i+2])
        myfile.close()
        i+=3
  
def updateStudent():                #VY
    deleteStudent()
    new_name = input("Please enter new name ")
    new_id = input("Please enter new ID ")
    new_gpa = input("Please enter new GPA ")
    update_new_student = Student(new_name, new_id, new_gpa)
    with open("data.txt", "a+") as data:
        data.write(new_id + "\n")
        data.write(new_name + "\n")
        data.write(new_gpa + "\n")
    print("Update success!")

def deleteStudent():               #PORTER
    id = input("Please enter student ID ")
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
    elif user_input == 'Update':
        updateStudent()
    elif user_input == "Delete":
        deleteStudent()
    elif user_input == 'Exit':
        break
    else :
        print("Invalid command, please try again")