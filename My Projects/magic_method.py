class book:
    place = ""

    def __init__(self,name,size,author):
        self.name = name
        self.size = size
        self.author = author
    def __str__(self):
        return f"{self.name} by {self.author}"
    def __eq__(self,other):
        return self.name == other.name and self.author == other.author

    @staticmethod
    def display_place(place):
        return f"the place work is {place}"
    

# so the magic method work with objects when you want change behavior between objects
    
book1 = book("harriboter",123,"same")
book2 = book("harriboter",320,"same")
print(book1.display_place("Algeria"))
print(book1 == book2)