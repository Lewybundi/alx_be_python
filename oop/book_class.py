# library_system.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __del__(self):
        print(f"Deleting {self.title}")


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year} [File Size: {self.file_size}KB]"
    
    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.year}, {self.file_size})"
    
    def __del__(self):
        print(f"Deleting {self.title}")


class PrintBook(Book):
    def __init__(self, title, author, year, page_count):
        super().__init__(title, author, year)
        self.page_count = page_count
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year} [Pages: {self.page_count}]"
    
    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.year}, {self.page_count})"
    
    def __del__(self):
        print(f"Deleting {self.title}")


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
    
    def __repr__(self):
        return f"Library({self.books})"
    
    def __del__(self):
        print("Deleting library")
        for book in self.books:
            book.__del__()