from errors import InvalidCharacterClass
class Character:
    CLASSES = ("Warrior", "Mage", "Priest", "Rogue")
    def __init__(self,name,genre,classinGame,weapon=None,item=None):
        self.Name=name
        self.Genre=genre
        if classinGame not in self.CLASSES:
            raise InvalidCharacterClass()
        self.ClassInGame=classinGame
        self.Weapon=weapon
        self.Item=item

    def print(self):
        print(f"Character name - {self.Name}/n"
              f"Character genre - {self.Genre}/n"
              f"Character calss - {self.ClassInGame}/n"
              f"{self.Weapon.print()}/n"
              f"{self.Item.print()}")