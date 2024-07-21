from typing import List

class Book:
    def __init__(self,title : str,author : str,isbn : str,published_year : int,available : bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_year = published_year
        self.available = available
    
    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False
    
    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False
    
    def get_info(self):
        if self.available == True:
            return f"Judul Buku : {self.title}, Penulis Buku : {self.author},Nomor ISBN : {self.isbn},Tahun Publikasi {self.published_year} Buku Masih Tersedia Untuk Di Pinjam"
        else:
            return f"Judul Buku : {self.title}, Penulis Buku : {self.author},Nomor ISBN : {self.isbn},Tahun Publikasi {self.published_year} Stok Buku Habis Sedang Di Pinjam"

class Member:
    def __init__(self,name : str,member_id : str,phone_number : str,email : str):
        self.name = name
        self.member_id = member_id
        self.phone_number = phone_number
        self.email = email
        self.borrowed_book : List[Book] = []
        
    def borrow_book(self,book : Book):
        if book.check_out():
            self.borrowed_book.append(Book)
            return True
        return False
    
    def return_book(self,book : Book):
        if book in self.borrowed_book:
            if book.return_book():
                self.borrowed_book.remove(book)
                return True
            return False
        
    def get_member_info(self):
        return f"name : {self.name},member id : {self.member_id},phone number : {self.phone_number},email : {self.email}"

class Library:
    def __init__(self,name : str, location : str):
        self.name = name
        self.location = location
        self.books : List[Book] = []
        self.members: List[Member] = []

    def add_book(self,book : Book):
        self.books.append(book)

    def remove_book(self,book : Book):
        if book in self.books:
            self.books.remove(book)
    
    def register_member(self,member : Member):
        self.members.append(member)

    def deregister_member(self,member : Member):
        if member in self.members:
            self.members.remove(member)

    def find_book(self, title : str) -> Book :
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def find_members(self,member_id : str) -> Member:
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
library = Library("Perpustakaan ITTP","Kampus Institut Telkom Purwokerto")
book1 = Book("Belajar Python","Muhamad Fikri","ISBN1",2024,True)
book2 = Book("Belajar Swift","Muhamad Fikri","ISBN2",2024,True)
member1 = Member("Nabil","234","088200647899","nabil@gmail.com")
member2 = Member("Awal","235","088200647456","awall@gmail.com")

library.add_book(book1)
library.add_book(book2)
library.register_member(member1)
library.register_member(member2)


member1.borrow_book(book1)
print(member1.get_member_info())
print(book1.get_info())

