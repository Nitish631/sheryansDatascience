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
                    Library.dummy_data=json.loads(content)
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
        Library.dummy_data['books'].append(book)
        Library.saveDummyData()
    def add_member(self):
        name=input("Enter the name: ")
        email=input("Enter the email: ")
        member={
            "id":Library.gen_id(Prefix="M"),
            "name":name,
            "email":email,
            "borowed":[]
        }
        Library.dummy_data["members"].append(member)
        Library.saveDummyData()
        print("Member added successfully.")
    def listBooks(self):
        if not Library.dummy_data["books"]:
            print("Sorry no Books Available.")
            return
        print(f"{"ID":12}{"TITLE":25}{"AUTHOR":24}{"TOTAL/AVAILABLE":20}{"ADDED ON"}")
        for b in Library.dummy_data["books"]:
            print(f"{b['id']:12}{b['title'][:24]:25}{b['author'][:12]:24}{(str(b['total_copies'])+"/"+str(b['available_copies'])):20}{b["added_on"]}")

    def listMembers(self):
        if not Library.dummy_data["members"]:
            print("Sorry no Members available.")
            return
        print()
        for m in Library.dummy_data["members"]:
            print(f"{"ID":12}{"NAME":15}{"EMAIL":20}")
            print(f"{m['id']:12}{m['name']:15}{m['email']:20}")
            print("This persion borrowed below books:")
            print(m['borowed'])
            print("\n\n")

    def borrowBooks(self):
        member_id=input("Enter the member id: ").strip()
        members=[m for m in Library.dummy_data["members"] if m['id']==member_id]
        if not members:
            print("No such ID exist for members.")
            return
        member=members[0]
        book_id=input("Enter the book id: ").strip()
        books=[b for b in Library.dummy_data["books"] if b['id']==book_id]
        if not books:
            print("No such ID exist for book.")
            return
        book=books[0]
        if book['available_copies']<=0:
            print("Sorry no books available right now.")
        borrow_entry={
            "book_id":book["id"],
            "title":book["title"],
            "borrow_on":datetime.now().strftime(format="%d/%m/%Y, %H:%M:%S")
        }
        member["borowed"].append(borrow_entry)
        book['available_copies']-=1
        Library.saveDummyData()
    def returnBook(self):
        member_id=input("Enter the member id: ").strip()
        members=[m for m in Library.dummy_data["members"] if m['id']==member_id]
        if not members:
            print("No such ID exist for members.")
            return
        member=members[0]
        if not member["borowed"]:
            print(f"No book borrowed by {member}")
            return
        print("Borrowed books")
        for i,b in enumerate(member['borowed'],start=1):
            print(f"{i}, {b['title']}  ({b['book_id']})")
        try:
            choice=int(input("enter number to return: - "))
            selected=member['borowed'].pop(choice-1)
        except Exception as e:
            print("Invalid value")
            return
        books=[bk for bk in Library.dummy_data["books"] if bk["id"]==selected["book_id"]]
        if books:
            books[0]["available_copies"]+=1
        Library.saveDummyData()
lib=Library()
choice=5
while choice!=0:
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
    print()
    if choice=="1":
        lib.add_book()
    if choice=="2":
        lib.listBooks()
    if choice=="3":
        lib.add_member()
    if choice=="4":
        lib.listMembers()
    if choice=="5":
        lib.borrowBooks()
    if choice=="6":
        lib.returnBook()
    if choice=="0":
        choice=0