# User Class
'''
User: A class to represent library users with attributes like name, library ID, and 
a list of borrowed book titles.
'''

class User():
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    # getters and setters

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_library_id(self):
        return self.library_id
    
    def set_library_id(self, library_id):
        self.library_id = library_id

    def borrow_book(self, book):
        self.borrowed_books.append
    
    def returned_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print(f"Error: Book {book} is not borrowed by this user")
    
    def show_borrowed_books(self):
        for book in self.borrowed_books:
            print(f"{book}")

    # display information
    
    def diplay_user(self):
        print(f"Name: {self.name}")
        print(f"Library ID: {self.library_id}")
        print(f"Borrowed Books: {User.show_borrowed_books()}")
    