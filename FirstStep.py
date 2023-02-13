class People:
    def __init__(self,age,gender,height):
        self.age = age
        self.gender = gender
        self.height = height
        
    def printdata(self):
        print(self.age)
        print(self.gender)
        print(self.height)

        
age = input()
gender = input()
height = input()



Junu = People(age,gender,height)

Junu.printdata()
