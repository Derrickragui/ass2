class Parent:
    __nationality = "Kenyan"
    def __init__(self,fname,lname):

        self.fname=fname
        self.lname=lname

    def printName(self):
        print(self.fname,self.lname)

class student(Parent):
    username= "Derrick"
    def doExams(self):
        print("I am doing exams")
    

newStudent = student("Derrick","Kuria")

print(newStudent.username,newStudent.nationality)
