class Book:
    def __init__(self,firstname,lastname,title,place,publisher,year):
        self.firstname=firstname
        self.lastname=lastname
        self.title=title
        self.place=place
        self.publisher=publisher
        self.year=year

    def write_bib_entry(self):
        return (self.lastname,self.firstname,self.title,self.place,self.publisher,self.year)

beauty = Book( "Dubay", "Thomas", "The Evidential Power of Beauty", "San Francisco", "Ignatius Press", "1999", )
pynut  = Book( "Martelli", "Alex", "Python in a Nutshell", "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )  

beauty.year="2021"
k=beauty.write_bib_entry()
print(k)
m=pynut.write_bib_entry()
print(m)