import random

def MovieCharacter()->str:
    movie_chars = [
            "Indiana Jones",
            "James Bond",
            "Han Solo", 
            "Batman", 
            "Ellen Ripley", 
            "The Joker", 
            "John McClane", 
            "Tyler Durden", 
            "Darth Vader", 
            "Marty McFly"
        ]
    return random.choice(movie_chars)