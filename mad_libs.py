import time

class Story:
    """
    Represents a Mad Libs story, including the template and required words.
    """
    def __init__(self, title, template, required_words):
        self.title = title
        self.template = template
        self.required_words = required_words
        self.user_words = {}

    def get_words_from_user(self):
        """Gets the required words from the user."""
        print(f"\n--- Please provide words for the '{self.title}' story ---")
        for word_type in self.required_words:
            self.user_words[word_type] = input(f"Enter a {word_type}: ")

    def generate_story(self):
        """Generates and prints the story with the user's words."""
        print("\n--- Here is your story! ---")
        time.sleep(2)
        print(self.template.format(**self.user_words))


class Game:
    """
    Manages the Mad Libs game flow.
    """
    def __init__(self):
        self.stories = self._load_stories()

    def _load_stories(self):
        """Loads the available stories."""
        story1_template = """
I will never forget the night it happened.
It was a(n) {adjective1} night, and I was relaxing upstairs with my {noun1}, a good book and my faithful {animal1} {petsname}.
Suddenly there was a loud {noise1}. I sprang to my feet and crept downstairs, trying to be as {adjective2} as I could.
Nothing looked out of the ordinary. Suddenly I heard the {noise1} again, but this time it was much more {adjective3} and I knew it was coming from the basement.
Summoning my courage, I grabbed a flashlight and strode {adverb1} down the stairs. I might have met my end right there, if not for {petsname}, who let out a loud "{noise2}!"
Startled, I jumped {adverb2} to the side just in time to avoid a long gooey appendage. I turned my flashlight on the intruder and gasped in horror.
Lurking there in my basement, bathed in the {adjective4} glow of my light, was a huge, quivering, shapeless blob of ooze! The hideous thing was as {colour1} as a {noun2} and as big as a(n) {noun3}. "{exclamation2}!" I cried.
I fled {adverb3} upstairs, but the thing chased me with lightning speed. I was trapped, and knew I had to fight if I wanted to survive.
First I tried to chop it with a {adjective7} {noun4} from the kitchen, then I shot it with my grandpas {noun5} that hangs over the fireplace.
In desperation, I even tried throwing {liquid} on it, but all to no avail. It just kept coming. I thought I was dead for sure, when suddenly a strange figure crashed through my window and leapt between us!
He was tall and {adjective5}, with fierce long eyes and sharp shoulders. He was dressed entirely in black, except for his {colour2} {clothing1}. "{exclamation1}!" the figure cried, and quick as a(n) {animal2} he jumped in and stunned the ooze creature with a powerful kick.
Without pause he scooped the thing into a(n) {noun6} and tied it shut with a {adjective6} {noun7}.
"How did you do that?!" I gasped, trying to catch my breath. "Their only weakness is their {bodypart1}," he replied. "One good kick and the things are helpless."
"But how do you find it?" I asked, staring at the shapeless mass. "That is easy," said the stranger. "It is right next to their {bodypart2}."
I thanked him for saving my life and asked him his name. "I am {foreignname}, and I have been hunting the ooze creatures all my life. Join me in my quest and we will make the world safe from their {adjective8} evil!"
Now that I knew the truth, how could I say no? I joined {foreignname} that night and my life has never been the same.
I learned how to spot their {bodypart1} in less than {num1} seconds, and together we have defeated over {num2} of the ooze creatures. I even got my own {colour2} {clothing1}.
"""
        story1_words = ["adjective1", "adjective2", "adjective3", "adjective4", "adjective5", "adjective6", "adjective7", "adjective8", "noun1", "noun2", "noun3", "noun4", "noun5", "noun6", "noun7", "clothing1", "noise1", "noise2", "foreignname", "bodypart1", "bodypart2", "colour1", "colour2", "liquid", "exclamation1", "exclamation2", "animal1", "animal2", "num1", "num2", "adverb1", "adverb2", "adverb3", "petsname"]

        story2_template = """
*knocks on table*...Hello!....I'm detective {malename}...and you are?
{teachername}
You're here today under suspicion of 2nd degree robbery.....
{exclamation1}!!!!
That's right...{num2} {plural2} were stolen from {storename} and the crime scene has your {body2} written all over it.
{exclamation2}!!!!
Where were you on the night of {holiday}?
I was watching {movie}
Then why does the crime scene footage show you {verb2} just {length} away from the crime scene?.......I'm through with playing games....Where are you from?!
{country}
..Yeah..You know the best part about being a detective is that I get to go home to my children and pet {pet} after locking up criminals like you and say {quote}
Fine...I did it..I commited the robbery but I only did it because I needed the money for my {bodypart2} surgery
I knew it all along...I knew it all along and every time I catch bastards like you I like to sing my favouraite song {childrensong}
Wow....You have a {adjective} voice!...I love you!
"""
        story2_words = ["malename", "teachername", "exclamation1", "exclamation2", "num2", "storename", "plural2", "body2", "holiday", "verb2", "movie", "length", "country", "pet", "quote", "bodypart2", "childrensong", "adjective"]

        return {
            "weird": Story("Weird", story1_template, story1_words),
            "crime": Story("Funny Crime", story2_template, story2_words)
        }

    def play(self):
        """Main function to play the game."""
        print("Welcome to Mad Libs Theatre!")

        while True:
            genre = input("Enter your genre from these options: a. Weird or b. Funny Crime: ").lower()

            if genre == 'a':
                story = self.stories["weird"]
            elif genre == 'b':
                story = self.stories["crime"]
            else:
                print("Invalid genre. Please choose 'a' or 'b'.")
                continue

            story.get_words_from_user()
            story.generate_story()

            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                break

        print("Thanks for playing!")


if __name__ == "__main__":
    game = Game()
    game.play()
