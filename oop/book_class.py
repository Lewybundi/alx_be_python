# library_system.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"Book: {self.title} by {self.author} ({self.year})"


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author} ({self.year}), File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, year, page_count):
        super().__init__(title, author, year)
        self.page_count = page_count
    
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author} ({self.year}), Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Can only add Book instances")
    
    def list_books(self):
        for book in self.books:
            print(book)