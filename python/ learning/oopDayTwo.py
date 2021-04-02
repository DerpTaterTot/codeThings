class Animal:
    name = "unknown"
    Type = "unknown"

    def printType(self):
        print("The animal,", self.name, "is a(n)", self.Type, "animal")


animals = [Animal(), Animal()]

animals[0].name, animals[0].Type = "orca", "ocean"
animals[1].name, animals[1].Type = "cheetah", "land"

animals[0].printType()
animals[1].printType()

