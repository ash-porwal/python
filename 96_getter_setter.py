'''
In classes we can change value of variables but in python we would change it with getter and setter - which 
gives us more information on how something should be changed and how something should be retrived
'''

class SomeClassName:
    def __init__(self, name:str) -> None:
        # I've made it a protected varibale with single underscore, 
        # so we dont want to access it outside class, 
        # but we can access it if we want but as a convention we dont want to do that
        self._name = name # the reason we made it protected because we want to only be access it through getters and setters

    # The @property decorator in Python is used to turn a method into a "getter" for a read-only attribute
    @property # here we created a property wrapper - this will help us modify the function with extra functionality
    def name(self) -> str:

        # so if we want to access self._name so we are accessing it with this function
        # and so here we can perform any modification to that name variable, 

        # so this will be the getter as we are getting the value from the class

        return self._name
    
    # we define setter as this -> @property_name.setter, 
    # and I've define name method as property name, so it will be name.setter. 
    # So, it also means before defining setter method we will need to define getter method as well.
    @name.setter 
    def name(self, new_name:str) -> None:
        # Setter method

        self._name = new_name

if __name__ == "__main__":
    
    # s = SomeClassName("Ashish")
    
    # this and s = SomeClassName("Ashish") both are same, here we added type hinting.
    # We're declaring that s should be of type SomeClassName and then immediately 
    # assigning an instance of the class to s.
    s: SomeClassName = SomeClassName("Ashish")
    print(s.name)

    s.name = "John" # sets a new name using the setter, without defining setter method on above we wouldn't be able to change that varibale value
