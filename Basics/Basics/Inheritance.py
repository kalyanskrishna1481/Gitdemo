from Basics.ClassesandObjects import Car


class Imp(Car):

    mess = "THis is importing from different class called as car"

    def __init__(self):

        Car.__init__(self, "racecar" ,"350mph" , "copany" )

    def getInh(self):
        return self.mess+ self.carType()

inher = Imp()
print(inher.getInh())

