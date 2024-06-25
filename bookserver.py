# This snippet represents a simplified version of the book catalog component.
class Book:
def __init__(self, title, author, price):
self.title = title
self.author = author
self.price = price

class BookCatalog:
def __init__(self):
self.books = []

def add_book(self, title, author, price):
book = Book(title, author, price)
self.books.append(book)

def search_books(self, keyword):
results = []
for book in self.books:
if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
results.append(book)
return results

# Usage example:
catalog = BookCatalog()
catalog.add_book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
catalog.add_book("To Kill a Mockingbird", "Harper Lee", 9.99)

keyword = input("Enter a keyword to search for books: ")
results = catalog.search_books(keyword)

for book in results:
print(f"Title: {book.title} | Author: {book.author} | Price: ${book.price}")