import json
import random
import string
from pathlib import Path
from datetime import datetime
from rich import print



class Library:
    database="CHAPTER1/PYTHON_PROJECT/library.json"
    dummy_data={"books":[],"members":[]}

    def __init__(self):
        ## LOAD EXISTING DATA TO JSON OR CREATE YOUR JSON
        if Path(Library.database).exists():
            with open(Library.database,"r")as f:
                content=f.read().strip()
                if content:
                    dummy_data=json.loads(content)
        else:
            with open(Library.database,"w") as f:
                json.dump(Library.dummy_data,f,indent=4)

    @classmethod
    def saveDummyData(cls):
        with open(cls.database,"w")as f:
            json.dump(cls.dummy_data,f,indent=4,default=str)

    def gen_id(Prefix="B"):
        random_id=""
        for i in range(5):
            random_id+=random.choice(string.ascii_lowercase+string.ascii_uppercase)
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
            "added_on":datetime.now().strftime(format="%d/%m/%Y, %H:%M:%S")
        }
        print(book)
        Library.dummy_data['books'].append(book)
        Library.saveDummyData()


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
if choice=="1":
    lib.add_book()