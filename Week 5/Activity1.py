class Book:
    def __init__(self, author, genre):
        self.author = author
        self.genre = genre
    
    def about_book(self):   
        print(f"Book information:\nAuthor: {self.author}\nGenre: {self.genre}\n")

class Programming(Book):
    def __init__(self, author, genre, title, language, published):
        super().__init__(author, genre)
        self.title = title
        self.language = language
        self.published = published

    def about_book(self):
        print(f'Book information:\n'
              f'Title: {self.title}\n'
              f'Author: {self.author}\n'
              f'Genre: {self.genre}\n'
              f'Language: {self.language}\n'
              f'Published: {self.published}\n')

class Novel(Book):
    def __init__(self, author, genre, title, pages):
        super().__init__(author, genre)
        self.title = title
        self.pages = pages

    def about_book(self):  
        print(f"Novel:\n"
              f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Genre: {self.genre}\n"
              f"Pages: {self.pages}\n")
        
books = [
    Programming("John Harris", "Programming", "Python Mastery", "English", 1989),
    Novel("Jane Austen", "Romance", "Pride and Prejudice", 432)
]

for book in books:   
    book.about_book()