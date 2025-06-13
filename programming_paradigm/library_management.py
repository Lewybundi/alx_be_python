class Book:
    """A class representing a book in a library system."""
    
    def __init__(self, title, author):
        """
        Initialize a book with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned/available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a book to the library's collection.
        
        Args:
            book (Book): The book to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if it's available.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                return book.check_out()
        return False
    
    def return_book(self, title):
        """Return a book by title if it was checked out.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                return book.return_book()
        return False
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
        else:
            for book in available_books:
                print(book)