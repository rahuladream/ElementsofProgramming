class Animal:
    def speaking(self):
        print("Animal Speaking")

class Dog(Animal):
    def barking(self):
        print("Dog Barking")

class DogChild(Dog):
    def eat_only(self):
        print("Dog child only eat")

if __name__ == "__main__":
    a = DogChild()
    a.speaking()
    a.barking()
    a.eat_only()