# Encapsulation in Python #
class Cars:

    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def setSpeed(self, value):
        self.__speed = value

    def getSpeed(self):
        return self.__speed

    def setColor(self, value):
        self.__color = value

    def getColor(self):
        return self.__color


ford = Cars(250, "Green")
nissan = Cars(300, "Red")
toyota = Cars(350, "Blue")

ford.setSpeed(450)
ford.setColor("Brown")

# Below two lines have no effect because speed and color are private.
ford.speed = 500
ford.color = "Pink"

print(ford.getSpeed())
print(ford.getColor())
