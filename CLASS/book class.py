class Book:
    book_title = None
    book_author = None
    publication_year = None
    current_year = int (2023)
    def __init__(self,title,auther,year):
        self.book_title = title
        self.book_author = auther
        self.publication_year = year

    def book_type(self):

        if self.current_year - self.publication_year > 50 :
            print(f"{self.book_title} is a classic book")
        else:
            print(f"{self.book_title} is not a classic book")

    def book_detarils(self):
        print(f"BOOK DETAILS:\n Tital:- {self.book_title}\n Book author :- {self.book_author}\n Publication Year:- {self.publication_year}")
        # return self.book_title ,self.book_author,self.publication_year

my_book  = Book(title="Wing of fire",auther= "APJ abdul kalam",year= 1950)
my_book.book_type()
print(my_book.book_detarils())
print(my_book.book_author)
