class publisher:
    "Information about the class"
    def __init__(self,publisher_name):
        self.publisher_name=publisher_name
        def display(self):
            pass
class book(publisher):
    def __init__(self,publisher_name,title,author):
        publisher.__init__(self,publisher_name)
        self.title=title
        self.author=author
    def display(self):
        pass
class python(book):
    def __init__(self,publisher_name,title,author,price,pageno):
        book.__init__(self,publisher_name,title,author)
        self.price=price
        self.pageno=pageno
    def display(self):
        print("Publisher name= ",self.publisher_name)
        print("Title= ",self.title)
        print("Author= ",self.author)
        print("Price= ",self.price)
        print("Page no= ",self.pageno)
s1=python("Pearson Education","Python Programming","Wesley",1500,800)
s1.display()
