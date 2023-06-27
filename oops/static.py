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
    
appu = Reader("Harry Potter and the Goblet of Fire")
appu.addBook("Bokya Satbande")
appu.addBook("Psychology of Money")

print(appu.__dict__)
print(Reader.TotalBooksRead)

satish = Reader("Cinderella")
satish.addBook("Ruskin Bond")
print(Reader.TotalBooksRead)

print(Reader.isLibraryOpen(4))