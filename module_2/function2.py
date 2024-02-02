import random

def Activity()->str:
    activities = [
        "Solving a mystery",
        "Planting a magical garden",
        "Inventing a new gadget",
        "Battling a mythical beast",
        "Exploring an ancient ruin",
        "Hosting a tea party for imaginary friends",
        "Cooking up a potion",
        "Building a spaceship from household items",
        "Chasing a rainbow to find the pot of gold",
        "Time-traveling to the future",
        "Painting a masterpiece",
        "Training a dragon",
        "Playing a board game with forest creatures",
        "Defeating a group of space invaders",
        "Dancing under the moonlight",
        "Searching for hidden treasure",
        "Helping a lost robot find its way home",
        "Learning a new spell",
        "Entering a parallel dimension",
        "Solving riddles to unlock a magical door"
    ]
    return random.choice(activities)