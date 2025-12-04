class Library:
    def __init__(self ):
        self.nobook = 0
        self.books = []
        print("This class has follwing function\nadd() -> to add the books\nshownum() -> To find the o of books\nshowbooks() -> To show the of books")

    def showbooks(self):
        print("Library has following books:")
        for i in self.books:
            print(i)
    
    def add(self,book):
        self.books.append(book)
        self.nobook=self.nobook + 1

    def shownum(self):
        print(f"Library has {self.nobook}")    
i=0
b = Library()
while i == 0:
    x = input("Ener the books")
    b.add(x)
    i = int(input("Enter the 1 to exit or enter the 0 to add more books"))
    if i == 1:
        break
b.showbooks()
b.shownum()

