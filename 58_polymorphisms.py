'''
Polymorphhism means ability to take various forms
'''

class Rectangle:
    def draw(self):
        print("Drawing a rectangle.")
     
     
class Triangle:
    def draw(self):
        print("Drawing a Triangle.")
     
     
 
# common interface
def draw_shape(Shape):
    Shape.draw()
 
#instantiate objects
A = Rectangle()
B = Triangle()
 
# passing the object
draw_shape(A)
draw_shape(B)

"""
In OOPs Polymorphisms is the ability of different objects to respond in their own way 
to the same method call.

1. Method Overriding (Subtype Polymorphism):
   This type of polymorphism occurs when a method in a derived class uses the same name 
   as a method in its superclass but implements a different functionality.
   The method in the subclass overrides the method in the superclass.

2. Duck Typing (Interface Polymorphism):
   Python implements what is often called "duck typing," 
   which is a type of polymorphism where the suitability of an object 
   for some purpose is determined by the presence of certain methods and properties, 
   rather than the actual type of the object.

3. Operator Overloading:
   Python also supports operator overloading, which is a specific case of polymorphism 
   where different operators have different implementations depending on their arguments. 
   For example, the + operator can add numbers, concatenate strings, or merge lists

"""

# overriding and duck typing
class Bird:
    def fly(self):
        print("Some birds can fly.")

class Parrot(Bird):
    def fly(self):
        print("Parrots can fly.")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly.")

def bird_flying_test(bird):
    bird.fly()

# Example of Polymorphism
parrot = Parrot()
penguin = Penguin()

bird_flying_test(parrot)  # Outputs: Parrots can fly.
bird_flying_test(penguin)  # Outputs: Penguins cannot fly.
