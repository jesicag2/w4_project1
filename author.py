# Author Class
'''
Author: A class representing book authors with attributes like name and biography.
'''

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    # getters and setters

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_biography(self):
        return self.biography
    
    def set_biography(self, biography):
        self.biography = biography

    # display information

    def display_author(self):
        print(f"Name: {self.name}")
        print(f"Biography: {self.biography}")
