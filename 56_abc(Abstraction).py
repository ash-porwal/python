from abc import ABC, abstractmethod

class first(ABC):
    @abstractmethod
    def fun1(self):
        pass
        # return "hello"
    
class second:
        def fun2(self):
            print("Namskar!")

class third(first, second):
        def fun1(self):
            print('Hello')
        def fun3(self):
            print("hmm")

# ash = first()
ash = third()
# ash = second()
ash.fun2()
ash.fun1()
ash.fun3()
# print(first.fun1("Ashish"))


'''
Summary:
Abstract method is a method which only has declaration and doesn't have definition.
A class is called abstract class only if it has at least one abstract method.
when you inherit an abstract class as a parent to the child class, the child class should define all the abstract method present in parent class.
if it is not done then child class also becomes abstract class automatically.
at last, python by default doesn't support abstract class and abstract method, so there is a package called ABC(abstract base classes) by which we can make a class or method abstract.
'''