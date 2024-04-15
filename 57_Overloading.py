"""
function overloading refers to the ability to have multiple functions 
with the same name but different parameters (different number or types of arguments). 

However, Python does not support traditional function overloading.

Why Python Doesn't Support?
if you define multiple functions with the same name, the last definition will override the previous ones. 
"""

class first:
    def fun1(self):
        print("The first")
    # def fun1(self,name):
    #     self.name = name
a = first()
a.fun1()