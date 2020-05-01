class Parent:
    def func1(self):
        print("This is function 1")

class Parent2:
    def func2(self):
        print("This is function 2")

class Child(Parent, Parent2):
    def func3(self):
        print("This is function 3")


if __name__ == "__main__":
    ob = Child()
    ob.func1()
    ob.func2()
    ob.func3()


# https://www.edureka.co/blog/inheritance-in-python/