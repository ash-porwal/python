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