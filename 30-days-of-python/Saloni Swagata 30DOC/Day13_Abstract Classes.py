from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

title=input("Enter the title of book: ")
author=input("Enter the name of author: ")
price=int(input("Enter the price of the book: "))
new_novel=MyBook(title,author,price)
new_novel.display()
