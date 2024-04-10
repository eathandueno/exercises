from dataclasses import dataclass

# must be coded before Book class, as Book class has an Authors type hint
# isn't a data class because has an attribute that's a list
class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)
    
@dataclass
class Book:
    title:str = ""
    authors:Authors = None

    def getDescription(self):
        return f"{self.title} by {self.authors}"
    
@dataclass
class Author:
    first_name: str = ""
    last_name: str = ""

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


