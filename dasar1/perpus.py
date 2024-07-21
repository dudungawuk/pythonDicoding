class Buku:
    def __init__(self, title: str, author: str, isbn: str, published_year: int, available: bool):
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
        if self.available:
            return f"Judul Buku: {self.title}, Penulis Buku: {self.author}, Nomor ISBN: {self.isbn}, Tahun Publikasi: {self.published_year}. Buku Masih Tersedia Untuk Dipinjam"
        else:
            return f"Judul Buku: {self.title}, Penulis Buku: {self.author}, Nomor ISBN: {self.isbn}, Tahun Publikasi: {self.published_year}. Stok Buku Habis, Sedang Dipinjam"

mybook = Buku("Dudung Sang Penjinak Ular", "Muhamad Fikri Nabil", "ssssssss", 2024, True)

print(mybook.get_info())
