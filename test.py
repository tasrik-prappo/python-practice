class Library:
    def __init__(self,name: str) -> None:
        self.name = name
        self.book: list[object] = []

    def add_book(self,book: object)-> None:
        self.book.append(book)

    def list_book(self) -> str:
        return [f"{book.title} by {book.author}" for book in self.book] 


class Book:
    def __init__(self,title: str, author: str):
        self.title = title
        self.author = author

library = Library("The North South Library")
book1 = Book("Harry Potter and Goblet of Fire","J.K. Rowling")
book2 = Book("Introduction to Calculus", "Howard Anton")
book3 = Book("Megnath", "Madhusudon Datta")

library.add_book(book1)
print(library.list_book())


