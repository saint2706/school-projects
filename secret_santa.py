import random

def get_participants():
    """
    Gets the list of participants from the user.

    Returns:
        list: A list of participant names.
    """
    participants = []
    while True:
        try:
            num_participants = int(input("Enter the number of participants: "))
            break
        except ValueError:
            print("Invalid number. Please enter a number.")

    for i in range(num_participants):
        name = input(f"Enter name of participant {i+1}: ")
        participants.append(name)

    return participants

def generate_pairings(participants):
    """
    Generates Secret Santa pairings.

    Args:
        participants (list): A list of participant names.

    Returns:
        dict: A dictionary of pairings (giver: receiver).
    """
    if len(participants) < 2:
        return None

    givers = list(participants)
    receivers = list(participants)

    random.shuffle(givers)
    random.shuffle(receivers)

    pairings = {}
    for giver in givers:
        receiver = receivers.pop(0)
        # If the giver is the same as the receiver, swap with the next receiver
        if giver == receiver:
            if receivers:
                receivers.append(receiver)
                receiver = receivers.pop(0)
            else:
                # This is the last person, so we need to swap with a previous pair
                # to avoid self-assignment.
                last_giver = list(pairings.keys())[0]
                pairings[giver] = pairings[last_giver]
                pairings[last_giver] = receiver
                continue

        pairings[giver] = receiver

    return pairings

def main():
    """
    Main function to run the Secret Santa generator.
    """
    print("--- Secret Santa Generator ---")
    participants = get_participants()

    if len(participants) < 2:
        print("You need at least two participants for Secret Santa.")
        return

    pairings = generate_pairings(participants)

    if pairings:
        print("\n--- Secret Santa Pairings ---")
        for giver, receiver in pairings.items():
            print(f"{giver} is the Secret Santa for {receiver}")
        print("---------------------------\n")
    else:
        print("Could not generate pairings.")

if __name__ == "__main__":
    main()
