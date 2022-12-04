
class InvalidParameterError(Exception):
    def __init__(self, e,*args):
        message = f"Invalid class parameter: {e}"
        super().__init__(message, *args)


class MissingParameterError(Exception):
    pass


#class InvalidAgeError(Exception,InvalidParameterError):
 #   def __init__(self,ex):
  #      super(InvalidAgeError, self).__init__(e)

# class InvalidSoundError(Exception,InvalidParameterError):
#   def __init__(self,ex):
#      super(InvalidAgeError, self).__init__(e)

class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.soind = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar:
    def __init__(self, name, age, sound):
        super.
