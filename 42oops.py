class RailwayForm: #class is the keyword for class
    formType = "RailwayForm"
    def printData(self): #yaha par function define hua hai...abhi ke liye  ye samjh lo ki self likhte hai
        print("Name is ", self.name) #yaha par ek fstring use kiya hai
        print(f"Train is {self.train}")

myApplication = RailwayForm() #here we did object instantiation..to yaha  ye bol raha ki ek mujhe naya form do...aur yaha par myApplication batata hai ki wo RailwayForm class ka object hai
myApplication.name = input("enter your name: ")
myApplication.train = "Rajdhani Express"
myApplication.printData()  # here we are calling the function 

'''
Just a note that method and function are not the same terms

function are not bound to any object and hence are not defined inside class
While Methods are bound to object and defined inside class

'''