class People:
    def __init__(self,age,gender,height):
        self.age = age
        self.gender = gender
        self.height = height
        
    def printdata(self):
        print(self.age)
        print(self.gender)
        print(self.height)

        
a = input()
b = input()
c = input()



Junu = People(a,b,c)

Junu.printdata()
