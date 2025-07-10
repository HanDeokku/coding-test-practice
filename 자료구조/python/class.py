class Car:
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed

    def speedUp(self):
        self.speed += 10

    def __str__(self):
        return "color : %s, speed : %d" % (self.color, self.speed)

car1 = Car('red', 10)

print("car1", car1)

class SuperCar(Car):
    def __init__(self, color, speed=0, bTurbo=True):
        super().__init__(color, speed)

    def setTurbo(self, bTurbo=True):
        self.bTurbo = bTurbo

    def __str__(self):
        if self.bTurbo:
            return "color : %s, speed : %d, 터보모드" % (self.color, self.speed)
        else:
            return "color : %s, speed : %d, 일반모드" % (self.color, self.speed)


car2 = SuperCar('blue', 100)

car2.setTurbo()

print("car2", car2)