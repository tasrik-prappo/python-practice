class Book:
    def __init__(self,title: str, author: str) -> None:
        self.title = title
        self.author = author



class Library:
    class Membership:
        def __init__(self, name: str, member_id: int) -> None:
            self.name = name
            self.member_id = member_id

    def  __init__(self, name: str, code: str, capacity: int) -> None:
        self.name = name
        self.books = []
        self.facility = Facility(code,capacity)
        self.members = []

    def add_books(self,book: object) -> None:
        self.books.append(book)

    def list_books(self) -> list[str]:
        return [f"{book.title} by {book.author}" for book in self.books] 

    def add_members(self,name: str, member_id: int) -> None:
        pass


class Facility:
    def __init__(self,code: str, capacity: int)-> None:
        self.code = code
        self.capacity = capacity



def main()-> None:
    pass

if __name__ == '__main__':
    main()