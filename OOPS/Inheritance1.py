class Animal:
    def speak(self):
        print("Animal Speaking")
    
class Dog(Animal):
    def bark(self):
        print("dog barking")


if __name__ == "__main__":
    d = Dog()
    d.bark()
    d.speak()