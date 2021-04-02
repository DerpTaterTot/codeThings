class Animal:
    name = "unknown"
    Type = "unknown"
    def __init__(self, name, Type):
        self.name = name
        self.Type = Type

    def printType(self):
        print("The animal,", self.name, "is a(n)", self.Type, "animal")


animals = [Animal("orca", "ocean"), Animal("cheetah", "land")]

animals[0].printType()
animals[1].printType()

