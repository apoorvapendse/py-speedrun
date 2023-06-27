# static methods are used when we don't want to pass object nor class as an arguement


class Reader:
    TotalBooksRead = 0;
    def __init__(self,bookName):
        self.booksRead = [bookName]
        Reader.TotalBooksRead+=1;

    def addBook(self,bookName):
        self.booksRead.append(bookName);
        Reader.TotalBooksRead+=1
        
    @classmethod
    def changeTotalBooksRead(cls,quantity):
        cls.TotalBooksRead = quantity;
    @staticmethod
    def isLibraryOpen(day):#here nothing is passed as arg whereas in class method, class is the arg and in instance method object is the arg
        if(day!=6):
            return True;
        return False;
    

# Visitor inherits all the properites and methods of Reader class
# And can also change the class variables of Reader class
class Visitor(Reader):
    def __init__(self, bookName,waitingTime):
        super().__init__(bookName)
        self.time = waitingTime
    # we can also override the parent class method using same function name to override it
    # similar to method overloading
ganesh = Visitor("Harry Potter",33)
print(ganesh.__dict__)
