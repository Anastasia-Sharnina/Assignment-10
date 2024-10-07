# Library.py

class Book:
    def __init__(self, title, author, year, price, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist

    def get_info(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: {self.price}, Stoplist: {self.stoplist}"

    @staticmethod
    def find_most_expensive(books):
        if not books:
            return None
        
        most_expensive = max(books, key=lambda book: book.price)
        return most_expensive

    def set_stoplist(self, value):
        self.stoplist = value

    def censor(self, author_name, value):
        if self.author == author_name:
            self.stoplist = value