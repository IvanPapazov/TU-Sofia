import random
class InvalidParameterError(Exception):
    def __init__(self, e,*args):
        message = f"Invalid class parameter: {e}"
        super().__init__(message, *args)


class MissingParameterError(Exception):
    pass


class InvalidAgeError(InvalidParameterError):
    def __init__(self,e,*args):
        message = f"Invalid class parameter: {e}"
        super().__init__(message, e,*args)


class InvalidSoundError(InvalidParameterError):
    def __init__(self, e, *args):
        message = f"Invalid class parameter: {e}"
        super().__init__(message, e, *args)


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        if name is None or age is None or sound is None:
            raise MissingParameterError()
        if type(name) is not str:
            raise InvalidParameterError("name")
        if type(age) is not int:
            raise InvalidAgeError("age")
        if type(name) is not str:
            raise InvalidSoundError("sound")

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super.__init__(name, age, sound)
        if self.age > 15:
            raise InvalidAgeError("age")
        if sound.count("r")>=2:
            raise InvalidSoundError("sound")

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for animal in animals:
            if type(animal) is Human or type(animal) is Lemur:
                animals.remove(animal)
                print(f"{self.name} the Jaguar hunted down {animal.name} the {type(animal).__name__}")


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super.__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError("age")
        if 'e' not in self.sound:
            raise InvalidSoundError("sound")

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self, fruits):
        if fruits >= 10:
            fruits -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits
        elif fruits > 0:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        else:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0


class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super.__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError("age")
        if 'e' not in self.sound:
            raise InvalidSoundError("sound")

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals, buildings):
        for i in range(len(animals)):
            if i > 0 and i < (len(animals)-1):
                if type(animals[i]) is self and type(animals[i-1]) is Human and type(animals[i+1]) is Human:
                    buildings.append(Building("AAA"))
            elif i == 0:
                if type(animals[i + 1]) is Human:
                    buildings.append(Building("BBB"))
            else:
                if type(animals[i - 1]) is Human:
                    buildings.append(Building("CCC"))



class Building:
    def __init__(self, typeBuilding):
        self.typeBuilding = typeBuilding


fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]


for i in range(102):
    try:
        rnd = random.randint(0, 9)
        age = random.randint(7, 20)
        name = random.randint(0, len(names) - 1)
        sound = random.randint(0, len(sounds) - 1)
        if rnd >= 0 and rnd <= 3:
            animals.append(Lemur(names[name], age, sounds[sound]))
        elif rnd > 3 and rnd <= 7:
            animals.append(Jaguar(names[name], age, sounds[sound]))
        elif rnd > 7 and rnd <= 9:
            animals.append(Human(names[name], age, sounds[sound]))
    except InvalidAgeError():
        print(f"{names[name]} {age} {sounds[sound]} {InvalidAgeError()}")
    except InvalidSoundError():
        print(f"{names[name]} {age} {sounds[sound]} {InvalidSoundError()}")
    except InvalidParameterError():
        print(f"{names[name]} {age} {sounds[sound]} {InvalidParameterError()}")
    except MissingParameterError():
        print(f"{names[name]} {age} {sounds[sound]} {MissingParameterError()}")

print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Lemur:
        fruits = anim.daily_task(fruits)
    if type(anim) == Jaguar:
        anim.daily_task(animals)
    if type(anim) == Human:
        anim.daily_task(animals, buildings)


print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
