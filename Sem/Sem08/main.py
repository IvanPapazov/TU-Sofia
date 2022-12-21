from Entities import character
from Sem08.Entities.errors import InvalidCommand,CharacterExists


class Menu:
    characters=[]
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a new weapon on character")
        print("3. Create a new item on character")
        print("4. Print all characters")
        print("5. Delete character")
        print("6. Exit")

    def command_create_character(self, name, sex, ch_class):
        pass

    def run(self):
        # infinite menu loop
        while True:
            self.print_menu()
            # ...

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:
                # process the user's choice
                if choice == "1":
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")
                    for i in character:
                        if name==i.Name:
                            raise CharacterExists()
                    sex = input("Enter the character genre (alpha-numeric): ")
                    ch_class = input("Enter the character name (alpha-numeric): ")
                    char = self.command_create_character(name,sex,ch_class)
                    self.characters(char)
                    # ...
                if choice == "6":
                    break
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':
    menu = Menu()
    menu.run()