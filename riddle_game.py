class RiddleGame:
    """
    Represents a riddle game.
    """
    def __init__(self):
        self.riddles = {
            "what is a table that you can eat": "vegetable",
            "it can be served but never eaten": "tennis ball",
            "the more you take the more you leave it behind": "footsteps",
            "it has many keys but no doors": "keyboard",
            "i am alive but donot need food,water can kill me": "fire"
        }
        self.points = 0
        self.target_points = 0

    def play(self):
        """Main function to play the game."""
        print("--- Riddle Game ---")
        print("There are 5 levels.")
        print("For a correct answer you get points ten times the round no.")
        print("For a wrong answer 25% of points of the round are deducted.")
        print("If you pass, no points are deducted.")

        while True:
            try:
                self.target_points = int(input("Enter your target points: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        for i, (riddle, answer) in enumerate(self.riddles.items()):
            print(f"\n--- Level {i+1} ---")
            print(riddle)

            guess = input("Enter your answer (or 'pass' to skip): ").lower()

            if guess == answer:
                print("Correct answer!")
                self.points += (i + 1) * 10
            elif guess == 'pass':
                print(f"The answer is: {answer}")
            else:
                print("Wrong answer!")
                self.points -= 0.25 * (i + 1) * 10

            print(f"Your points: {self.points}")

        print("\n--- Game Over ---")
        if self.points >= self.target_points:
            print("Well played! You reached your target.")
        else:
            print("Good try! Better luck next time.")

if __name__ == "__main__":
    game = RiddleGame()
    game.play()
