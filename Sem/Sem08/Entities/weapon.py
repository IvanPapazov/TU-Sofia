class Weapon:
    def __init__(self,attack):
        self.Attack=attack

    def print(self):
        return f"Attack - {self.Attack}"