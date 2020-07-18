from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    title = ""
    author = ""
    price = ""
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        print("Title:", title)
        print("Author:", author)
        print("Price:", price)

title=input()
