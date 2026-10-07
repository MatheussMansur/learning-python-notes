class Animal:
    pass


class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Blub"

    def __str__(self):
        return "Hello, my name is " + self.name


class ClownFish(Fish):
    pass


class TangFish(Fish):
    def speak(self):
        return "Hello, I'm a TangFish"


nemo = ClownFish("Nemo")
dory = TangFish("Dory")

print(nemo, "-", nemo.speak())
print(dory, "-", dory.speak())
print(isinstance(nemo, Animal), isinstance(nemo, TangFish))
