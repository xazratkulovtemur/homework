# Custom Exceptions
class BookNotFoundException(Exception):
    """Raised when the requested book is not found in the library."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Raised when a book is already borrowed by someone else."""
    pass

class MemberLimitExceededException(Exception):
    """Raised when a member tries to borrow more than the allowed limit."""
    pass

# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Initially, the book is available

    def borrow(self):
        if self.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{self.title}' is already borrowed.")
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: {self.title} by {self.author} ({status})"

# Member Class
class Member:
    MAX_BORROW_LIMIT = 3  # Members can borrow up to 3 books

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to store borrowed book titles

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} has already borrowed {self.MAX_BORROW_LIMIT} books.")
        book.borrow()
        self.borrowed_books.append(book.title)

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {', '.join(self.borrowed_books) if self.borrowed_books else 'None'}"

# Library Class
class Library:
    def __init__(self):
        self.books = {}   # Dictionary to store books {title: Book object}
        self.members = {} # Dictionary to store members {name: Member object}

    def add_book(self, book):
        self.books[book.title] = book

    def add_member(self, member):
        self.members[member.name] = member

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"'{book_title}' is not available in the library.")
        if member_name not in self.members:
            print(f"Member '{member_name}' is not registered. Registering first...")
            self.add_member(Member(member_name))  # Auto-register if not found
        member = self.members[member_name]
        book = self.books[book_title]
        member.borrow_book(book)
        print(f"{member_name} successfully borrowed '{book_title}'.")

    def return_book(self, member_name, book_title):
        if member_name not in self.members or book_title not in self.books:
            raise BookNotFoundException(f"Invalid return request. Check the book or member.")
        member = self.members[member_name]
        book = self.books[book_title]
        member.return_book(book)
        print(f"{member_name} successfully returned '{book_title}'.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(book)

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members.values():
            print(member)

# Testing the System
if __name__ == "__main__":
    library = Library()

    # Adding Books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    book4 = Book("Moby Dick", "Herman Melville")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Adding Members
    member1 = Member("Alice")
    member2 = Member("Bob")
    library.add_member(member1)
    library.add_member(member2)

    # Display Books and Members
    library.display_books()
    library.display_members()

    print("\n===== Borrowing Books =====")
    try:
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        # Alice tries to borrow more than 3 books (should raise an exception)
        library.borrow_book("Alice", "Moby Dick")
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Bob tries to borrow a book that doesn't exist
        library.borrow_book("Bob", "Harry Potter")
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Bob tries to borrow a book that Alice already borrowed
        library.borrow_book("Bob", "The Great Gatsby")
    except Exception as e:
        print(f"Error: {e}")

    # Display Members after borrowing
    library.display_members()

    print("\n===== Returning Books =====")
    try:
        library.return_book("Alice", "The Great Gatsby")
        library.return_book("Alice", "1984")
        # Alice tries to return a book she didn’t borrow
        library.return_book("Alice", "Moby Dick")
    except Exception as e:
        print(f"Error: {e}")

    # Display final status
    library.display_books()
    library.display_members()
