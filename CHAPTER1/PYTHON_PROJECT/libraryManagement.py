import json
import random
import string
from pathlib import Path
from datetime import datetime



class Library:
    def gen_id(Prefix="B"):
        random_id=""
        for i in range(5):
            random_id+=random.choices(string.ascii_lowercase+string.ascii_uppercase)
        return Prefix+"-"+random_id
    def add_book(self):
        title=input("Enter the book title: ")
        author=input("Enter the book author: ")
        copies=int(input("How many copies: "))
        book={
            "id":Library.gen_id(),
            "title":title,
            "author":author,
            "total_copies":copies,
            "available_copies":copies,
            "added_on":datetime.now().strftime()
        }
        print(book)


lib=Library()
print("="*50)
print("LIBRARY MANAGEMENT SYSTEM")
print("="*50)
print("""
1. Add Book
2. List Book
3. Add Members
4. List Members
5. Borrow Book
6. Return Book
0. Exit the portal
""")
print("-"*50)
choice=input("What task you want to do? ")
if choice==1:
    lib.add_book()