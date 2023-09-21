#!/usr/bin/env python
"""Script flow and debugging. Find a fortune!"""


import random


DIVEFINDS = [
    "engagement rings 💍 and other rings ",
    "completely ruined mobile phones 📱",
    "⌚ Apple, Rolex, and Timex watches",
]


def generate_find() -> str:
    """Use a random selection to determine the scuba diver's find."""
    return random.choice(DIVEFINDS)


def calculate_number_items(number_dives):
    """Returns the multiplier for the random amounts of found objects."""
    how_many = random.randint(1, 15)
    dive_items = how_many * number_dives
    
    return dive_items


def create_dive_finds(number_dives):
    """Make and return the items the scuba diver finds in this dive.

    The message should include the diver's find and amounts.
    """
    # TODO: Create a message telling a scuba diver what they found by 
    # calling generate_find() and calculate_number_items() and 
    # then composing and returning the message and numbers.
    find = generate_find()
    number_items = calculate_number_items(number_dives)
    #dive_finds_message = find + ": " + str(number_items)
    #dive_finds_message = "In "+ str(number_dives) + " dives, you found " + str(number_items) + " " + find
    dive_finds_message = "In {} dives, you found {} {}".format(number_dives, number_items, find)
    #raise NotImplementedError()
    return dive_finds_message

def main():
    """Explain the scuba diver game in a command prompt."""
    print("You're a scuba diver, let's see what you find on your dives today!")

    # Prompt the user for how many dives they are going on
    number_dives = input("How many dives are you taking today?  ")
    number_dives = int(number_dives.strip())

    # Create and display their finds
    dive_finds_message = create_dive_finds(number_dives)
    print("\nHere are your finds, you lucky diver!\n")
    print(dive_finds_message)


if __name__ == '__main__':
    main()

