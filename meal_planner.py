import random

def get_user_preferences():
    """
    Gets the user's dietary preferences.

    Returns:
        dict: A dictionary of user preferences.
    """
    preferences = {}
    preferences['long_travel'] = input("Have you traveled by flight for more than 3 hours (yes/no)? ").lower() == 'yes'
    preferences['diabetic'] = input("Are you diabetic (yes/no)? ").lower() == 'yes'
    preferences['jain'] = input("Are you a jain (yes/no)? ").lower() == 'yes'
    return preferences

def generate_meal_plan(preferences):
    """
    Generates a meal plan based on user preferences.

    Args:
        preferences (dict): A dictionary of user preferences.
    """
    breakfast_options = ["Oatmeal", "Scrambled Eggs", "Pancakes", "Cereal"]
    lunch_options = ["Salad", "Sandwich", "Soup", "Pasta"]
    dinner_options = ["Stir-fry", "Grilled Chicken", "Fish", "Tofu"]

    breakfast = random.choice(breakfast_options)
    lunch = random.choice(lunch_options)
    dinner = random.choice(dinner_options)

    meal_plan = {
        "Breakfast": breakfast,
        "Lunch": lunch,
        "Dinner": dinner
    }

    additions = []
    subtractions = []

    if preferences['long_travel']:
        additions.append("water")
    if preferences['diabetic']:
        additions.append("fruits, vegetables and whole grains")
    if preferences['jain']:
        subtractions.append("onion and garlic")

    print("\n--- Your Meal Plan ---")
    for meal, item in meal_plan.items():
        meal_str = f"{meal}: {item}"
        if additions:
            meal_str += " + " + ", ".join(additions)
        if subtractions:
            meal_str += " - " + ", ".join(subtractions)
        print(meal_str)
    print("--------------------")

def main():
    """
    Main function to run the meal planner.
    """
    while True:
        preferences = get_user_preferences()
        generate_meal_plan(preferences)

        play_again = input("\nGenerate another meal plan? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Enjoy your meals!")

if __name__ == "__main__":
    main()
