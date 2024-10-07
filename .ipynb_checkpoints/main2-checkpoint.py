# main.py

from Library import Book

# Create a list of different books
books = [
    Book("1984", "George Orwell", 1949, 15.99),
    Book("Brave New World", "Aldous Huxley", 1932, 18.50),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 10.99),
    Book("To Kill a Mockingbird", "Harper Lee", 1960, 12.99),
    Book("Moby Dick", "Herman Melville", 1851, 20.00)
]

# Display information about each book
print("Book Information:")
for book in books:
    print(book.get_info())

# Find and display the most expensive book
most_expensive_book = Book.find_most_expensive(books)
if most_expensive_book:
    print("\nMost Expensive Book:")
    print(most_expensive_book.get_info())

# Set stoplist for a specific book
books[0].set_stoplist(True)  # Setting stoplist for "1984"
print("\nAfter setting stoplist for '1984':")
print(books[0].get_info())

# Censor a book by author name
books[1].censor("Aldous Huxley", True)  # Censoring "Brave New World"
print("\nAfter censoring 'Brave New World':")
print(books[1].get_info())
