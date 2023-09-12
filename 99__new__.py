# with __new__ we can block two objects creation of the same class

class SomeClass:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("Connecting with new instance")
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print("There is already one connection going on")
            return cls.__instance
    
    def __init__(self) -> None:
        print(f"Object Connected with {self}")

# lets try to conncet SomeClass with two different objects

a = SomeClass()
b = SomeClass()