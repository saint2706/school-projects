import random
import time

class Magic8Ball:
    """
    Represents a Magic 8-Ball game with a roast feature.
    """
    def __init__(self):
        self.responses = [
            "Absolutely", "Answer Unclear Ask Later", "Cannot Foretell Now", "Can't Say Now",
            "Chances Aren't Good", "Consult Me Later", "Don't Bet On It", "Focus And Ask Again",
            "Indications Say Yes", "Looks Like Yes", "No", "No Doubt About It", "Positively",
            "Prospect Good", "So It Shall Be", "The Stars Say No", "Unlikely", "Very Likely",
            "Yes", "You Can Count On It"
        ]
        self.roasts = [
            "U R THE REASON INDIA IS CONSIDERED A 3RD WORLD COUNTRY",
            "UR MAMA SO POOR, SHE CANT EVN PAY ATTENTION",
            "*KEEPS MIRROR IN FRONT OF USER*",
            "UR ASS MUST BE SO JEALOUS OF ALL THE SH!T THAT COMES THROUGH UR MOUTH",
            "IF LAUGHTER IS THE BEST MEDECINE,UR FACE MUST CURING THE WORLD",
            "UR FAMILY TREE MUST BE A CACTUS COZ EVERYONE ON IT IS A PRICK",
            "UR BIRTH CERTIFICATE IS AN APOLOGY LETTER FROM THE CONDOM FACTORY",
            "U R LIVING PROOF THAT EVN GOD ISNT PERFECT AND MAKES MISTAKES",
            "U MUSTVE BEEN BORN IN AN EXAM HALL COZ THATS WHERE LOTS OF PEOPLE MAKE MISTAKES",
            "THE ONLY WAY U WILL EVR GET LAID IS IF U CRAWL UP A CHICKEN'S ASS AND WAIT",
            "U R AN OXYGEN THIEF",
            "THEY SAY OPPOSITES ATTRACT SO I HOPE U MEET SOMEONE WHO IS INTELLIGENT, GOOD LOOKING AND WELL-CULTURED",
            "YOU HAVE DIARRHEA OF THE MOUTH AND CONSTIPATION OF SMARTNESS",
            "LAST TIME I SAW SOMETHING LIKE U, I FLUSHED IT",
            "IF U REALLY SPOKE UR MIND, U WILL BE SPEECHLESS",
            "JUST COZ U HV ONE DOESNT MEAN U HV TO BE ONE"
        ]

    def play(self):
        """Main function to play the game."""
        print("--- Magic 8-Ball ---")

        while True:
            question = input("Ask the Magic 8-Ball a question, type 'roast me' for a roast, or 'quit' to exit: ").lower()

            if question == 'quit':
                break
            elif question == 'roast me':
                print("Shaking...")
                time.sleep(2)
                print("All the best...")
                time.sleep(1)
                print(f"\n{random.choice(self.roasts)}\n")
            else:
                print("Thinking...")
                time.sleep(2)
                print(f"\n{random.choice(self.responses)}\n")

            print("Disclaimer: Don't rely on these answers, it's just a random answer.\n")

if __name__ == "__main__":
    game = Magic8Ball()
    game.play()
    print("Thanks for playing!")
