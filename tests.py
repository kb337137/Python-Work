def sayhello(a,b):
    return a+b

class sameer():
    def __init__(self,name,father,email):
        self.name = name
        self.father = father 
        self.email = email
    def Details(self):
        print(f"Student :{self.name} , Father :{self.father} Email :{self.email}")



class Student():
    def __init__(std,Name,FatherName,Email):
        std.studentName = Name
        std.fathername = FatherName
        std.Email = Email
    
    def study(std):
        print(f"{std.studentName} Kar Sakta Han")
    def Work(std):
        print(f"{std.studentName}Wo Assignment Kar Sakta han")
        
        
__name__ = "Name Change"