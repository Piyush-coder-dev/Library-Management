# Library management !
import json
import os
import sys

class Library:
    def __init__ (self):
        self.books = []
        self.NoOfBooks = len(self.books)
        # loading books
        if os.path.exists(os.path.join(os.getcwd(), "books.json")):
            with open(os.path.join(os.getcwd(), "books.json"), "r") as f:
                self.books = json.load(f)
        else:
            with open(os.path.join(os.getcwd(), "books.json"), "w") as f:
                pass

    def showBooks(self):
        print(f"\nThere are {len(self.books)} Books : \n")
        for book in self.books:
            print(f"name : {book["name"]}")
            print(f"author : {book["author"]}\n")

    def addBooks(self, bookName, authorName):
        self.book = bookName.title()
        self.author = authorName.title()

        self.books.append({"name": self.book, "author": self.author})
        self.uniqueBooks = []

        for book in self.books:
            if book not in self.uniqueBooks:
                self.uniqueBooks.append(book)

        self.books = self.uniqueBooks

        with open("books.json", "w") as file:
            json.dump(self.books, file, indent=4)
            print(f'\n{self.book} Added Successfully !')

    def removeBooks(self, book_name, author_name):
        # Python is case sensitive so capitalizing all letter by using .title() to match

        remove_book = {"name": book_name.title(), "author": author_name.title()}
        self.nbooks = list(filter(lambda book: book != remove_book, self.books))
        
        self.bookNotFound = False

        if remove_book not in self.books:
            self.bookNotFound = True
        else:
            self.bookNotFound = False

        self.books = self.nbooks

        with open("books.json", "w") as file:
            json.dump(self.books, file, indent=4)
        
        if self.bookNotFound:
            print(f'{book_name.title()} not Found in Library !')
        else:
            print(f'{book_name.title()} has been removed !')

    def showNoOfBooks(self):
        print(f'There are {len(self.books)} in Your Library')

app = Library()

keys_ = ["Add Books", "Remove Books", "Show Books", "Show No. of Books", "Exit"]
print("\nWelcome to Your Library Management!\n")
for index, item in enumerate(keys_):
    print(f"Enter {index} to {item} !")

while True:

    query = int(input("\nEnter Here : ").strip())

    if query == 4:
        sys.exit()

    elif query == 0:
        print("Provide the Book details to Add !")
        bookName = input("Enter Book Name : ").strip()
        authorName = input("Enter Author Name : ").strip()
        if len(bookName) > 0 and len(authorName) > 0:
            app.addBooks(bookName, authorName)
        elif len(bookName) > 0 and len(authorName) <= 0:
            print("\nPlease Provide The Author Name !, Can't Add the Book without it")
        elif len(bookName) <= 0 and len(authorName) > 0:
            print("\nPlease Provide The Book Name !, Can't Add the Book without it")

    elif query == 1:
        print("Provide the Book details to remove !")
        bookName = input("Enter Book Name : ").strip()
        authorName = input("Enter Author Name : ").strip()
        print(f'\nAre You Sure ?, You want to remove {bookName.title()} from Your Library!')
        x = int(input("Enter 9 to proceed and 8 to cancel : ").strip())
        
        if x == 9:
            app.removeBooks(bookName, authorName)
        else:
            print(f"Thank You for Not Removing {bookName.title()} from Your Library!")

    elif query == 2:
        app.showBooks()

    elif query == 3:
        app.showNoOfBooks()