'''
---------------------------------------------------------------------------------------
Imagine you're designing a software system for a zoo. 
You decide to have a base class called Animal since all entities in the zoo are animals. 
Now, every animal can make_sound, but the specific sound each animal makes is different.
---------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------
Here's where abstract methods come into play. 
You know every animal should be able to make_sound, 
but you can't define a generic sound for the base Animal class because it doesn't make sense. 
An abstract method lets you declare that a method should exist, without providing an implementation.
---------------------------------------------------------------------------------------
'''

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

'''
---------------------------------------------------------------------------------------
Now, when you create specific animal classes, 
you will be forced to define the make_sound method for each one.
This ensures consistency across all subclasses.
---------------------------------------------------------------------------------------
'''

class Lion(Animal):

    def make_sound(self):
        return "Roar!"

class Bird(Animal):

    def make_sound(self):
        return "Chirp!"


'''
---------------------------------------------------------------------------------------
By using an abstract method, you ensure:

Consistency: Every subclass must provide an implementation for make_sound.
Clarity: Anyone reading the code knows that any Animal should be able to make_sound, 
even if the base Animal class doesn't specify how.

so, what I understand is, 
we define abstract class just to make other class to follow the mandatory functions which are needed.
---------------------------------------------------------------------------------------
'''

'''
---------------------------------------------------------------------------------------
To reiterate, 
by using abstract classes and methods, you're essentially saying: 
Any class that inherits from this abstract class must provide specific functionalities, 
but it's up to that class to decide how to implement them.
This combination of enforcement and flexibility is a powerful tool in object-oriented design.
---------------------------------------------------------------------------------------
'''