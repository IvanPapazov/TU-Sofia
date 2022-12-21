class Item:
    def __init__(self,durability=100):
        self.Durability=durability

    def print(self):
        return f"Durability - {self.Durability}"