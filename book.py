# Book Class
'''
Book Class: A class representing individual books with attributes such as title, author, 
ISBN, genre, publication date, and availability status.
'''

class Book():
    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True

    # getters and setters

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.title = author

    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn):
        self.title = isbn
    
    def get_genre(self):
        return self.genre
    
    def set_genre(self, genre):
        self.title = genre

    def get_publication_date(self):
        return self.publication_date
    
    def set_publication_date(self, publication_date):
        self.title = publication_date

    def get_availability(self):
        return self.availability
    
    def set_availability(self, availability):
        self.title = availability

    # display of information

    def display_books(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Genre: {self.genre}")
        print(f"Publication Date: {self.publication_date}")
        if self.availability == True:
            print("Availability: Available")
        else:
            print("Availability: Not Available")