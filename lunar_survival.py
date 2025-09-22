class LunarSurvivalGame:
    """
    Represents a text-based lunar survival game.
    """
    def __init__(self):
        self.items = {
            "A": "3 litres of water",
            "B": "Shampoo",
            "C": "An extra Spacesuit",
            "D": "A shovel",
            "E": "A 10 day oxygen supply",
            "F": "Solar panels",
            "G": "The seeds for your mission",
            "H": "The soil for your mission",
            "I": "A 3 day food supply",
            "J": "A satellite phone"
        }
        self.survival_items = ["A", "E", "F", "I"]

    def play(self):
        """Main function to play the game."""
        print("It is the year 2050. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
        print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
        print("You can get to the base in 3 days on your lunar rover")
        print("The lunar rover can only fit you in your spacesuit and 4 other items")
        print("Out of the items below, which do you bring? \n")

        for key, value in self.items.items():
            print(f"{key}: {value}")

        print("\nType the letter of the 4 items you would like to bring separated by commas.\nDo not add spaces \nEx: A,B,C,D")

        while True:
            user_choice = input("Enter your choice: ").upper()
            user_list = list(user_choice.split(','))

            if len(user_list) == 4:
                break
            else:
                print("Please select exactly 4 items.")

        if "A" not in user_list:
            print("Without a litre of water a day you will dehydrate")
        if "E" not in user_list:
            print("Without oxygen you will not have any air to breathe!")
        if "F" not in user_list:
            print("Without solar panels your lunar rover will not have enough power to make it to the base")
        if "I" not in user_list:
            print("You will not make it to the moon base without food. You will need your energy to drive the rover.")

        if all(item in user_list for item in self.survival_items):
            print("\nHooray! You picked the correct 4 items. You will make it to the moonbase safely")
        else:
            print("\nYou did not pick the correct 4 items for survival. You will not make it safely to the moon base.")

if __name__ == "__main__":
    game = LunarSurvivalGame()
    game.play()
