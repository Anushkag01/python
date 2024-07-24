class Author:
    def __init__(self, name):
        self.name = name
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
author1 = Author("J.K. Rowling")
book1 = Book("Harry Potter and the Sorcerer's Stone", author1)
# Accessing Book and Author attributes
print(f"The book '{book1.title}' was written by {book1.author.name}")
