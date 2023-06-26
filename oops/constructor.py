class Student:
    division='O'#class var
    students = 0;
    # below is the syntax of constructor and self is the current object of the class
    def __init__(self,fname,lname,branch):
        self.firstName = fname;
        self.lastName = lname;
        self.shakha = branch 
        self.division = 'C'
        Student.students +=1 #increment number of students(class var) by 1 whenever constructor is called
  
    def tellDiv(self):
        print(self.division)
        print(Student.division)

appu = Student("Apoorva","Pendse","IT");#creating an object of class Student and passing the arguements to the constructor
srupat = Student("Sru","Pat","CS");

appu.os = "linux"
appu.tellDiv()
print(appu.__dict__)#it will also print the os instance var
# __dict__ lists all the variables of a given object of class

# to print all the class vars instead of instance vars
print(Student.__dict__)

print(Student.students)