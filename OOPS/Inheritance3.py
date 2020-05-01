class Parent:
    def __init__(self, fname, fage):
        self.fname = fname
        self.age = fage
    
    def view(self):
        print(self.fname, self.age)
    

class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lname = "Edureka"
    
    def view(self):
        print("Course Name", self.fname, "first came", self.age, " years ago", self.lname, "has courses master python")



if __name__ == "__main__":
    ob = Child("Python", '28')
    ob.view()