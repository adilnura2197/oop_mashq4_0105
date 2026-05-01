class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print("Kitob o‘qilmoqda")


class EBook(Book):
    def __init__(self, title, author, pages, file_size, format_type):
        super().__init__(title, author, pages)
        self.file_size = file_size
        self.format_type = format_type

    def read(self):
        super().read()
        print(f"Nomi: {self.title}")
        print(f"Muallif: {self.author}")

    def download(self):
        print(f"Fayl yuklanmoqda ({self.file_size}MB)")


e1 = EBook("Python 101", "Ali", 200, 5, "PDF")

e1.read()
e1.download()
