class Animal:
    def speak(self):
        print("This animal makes a generic sound")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow")

# Creating instances
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Calling the method
generic_animal.speak()  # Outputs: This animal makes a generic sound
dog.speak()             # Outputs: Dog says: Woof woof!
cat.speak()             # Outputs: Cat says: Meow
