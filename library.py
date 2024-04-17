# Library Management System
from book import Book
from user import User
from author import Author

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("What would you like to do: ")

            if choice == '1':
                self.book_menu()
            elif choice == '2':
                self.user_menu()
            elif choice == '3':
                self.author_menu()
            elif choice == '4':
                print("Goob bye! Thanks for using the Library Management System!")
                break
            else:
                print("Error: Please enter a valid option.")

    def book_menu(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("What would you like to do: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter Author name: ")
                isbn = input("Enter ISBN: ")
                genre = input("Enter book genre: ")
                publication_date = input("Enter book publication date")
                self.add_book(title, author, isbn, genre, publication_date)
            elif choice == '2':
                title = input("Enter book title you would like to borrow: ")
                self.borrow_book(title)
            elif choice == '3':
                title = input("Enter book title you would like to return: ")
                self.return_book(title)
            elif choice == '4':
                title = input("Enter book title you would like to search: ")
                self.search_book(title)
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Error: Please enter a valid option.")

    def user_menu(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("What would you like to do: ")

            if choice == '1':
                name = input("Enter name of new member: ")
                library_id = input("Enter their new library id: ")
                self.add_user(name, library_id)
            elif choice == '2':
                library_id = input("Enter library id of member you would like to view: ")
                self.view_user(library_id)
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Error: Please enter a valid option.")

    def author_menu(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("What would you like to do: ")

            if choice == '1':
                name = input("Enter name of author: ")
                biography = input("Enter author biography: ")
                self.add_author(name, biography)
            elif choice == '2':
                name = input("Enter author you would like to view: ")
                self.view_author(name)
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Error: Please enter a valid option.")

    # book operations

    def add_book(self, title, author, isbn, genre, publication_date):
        new_book = Book(title, author, isbn, genre, publication_date)
        self.books.append(new_book)
        print("Book added successfully!")

    def borrow_book(self, title):
        for book in self.books:
            if book.get_title() == title and book.get_availability():
                book.set_availability(False)
                print(f"Book '{title}' has been borrowed successfully.")
                return
        return None

    def return_book(self, title):
        for book in self.books:
            if book.get_title() == title and not book.get_availability_status():
                book.set_availability_status(True)
                print(f"Book '{title}' has been returned successfully.")
                return
        return None

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book {title} is here at our library")
                return book
        print("Book not found at our library.")
    
    def display_all_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("The books in the library:")
            for book in self.books:
                book.display_books()

    # user operations
    
    def add_user(self, name, library_id):
        new_user = User(name, library_id)
        self.users.append(new_user)
        print("Member has been added successfully!")
    
    def view_user(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                user.display_user()
                return
        print("Member not found.")

    def display_all_users(self):
        if not self.users:
            print("No members available in the library.")
        else:
            print("Members currently enrolled in the library:")
            for user in self.users:
                user.display_user()

    # author operations

    def add_author(self, name, biography):
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print("Author has been added successfully!")

    def view_author(self, name):
        for author in self.authors:
            if author.get_name() == name:
                author.display_author()
                return
        print("Author not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors available in the library.")
        else:
            print("List of authors in the library:")
            for author in self.authors:
                author.display_author()

library = Library()
library.main_menu()