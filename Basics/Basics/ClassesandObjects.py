

class pract:
    num = 123


    def __init__(self, c, d):
        print("this is a default constructor")
        self.cds = c
        self.dsf = d

    def gdata(self):
        a = 12
        b = 24
        return a + b

    def sum(self):
        return self.cds+self.dsf+pract.num+1


object1 = pract(4, 65)
print(object1.gdata())
print(object1.num)
print(object1.sum())
print


class Car:

    def __init__(self, tpe, speed, copany):
        self.typ = tpe
        self.sped = speed
        self.comp = copany

    def carType(self):
        print("This is the details you were supposed to get after clicking this")
        return self.typ+" "+self.comp+" "+self.sped




car1 = Car("Sedan", "230kph", "Hyundai")
print(car1.carType())

car2 = Car("Hatchback", "260kph", "Hyundai")
print(car2.carType())


