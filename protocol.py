from typing import Protocol
import os, random

class RandomInfo (Protocol):

    def rand_first_info(self):
        ...
    
    def rand_second_info(self):
        ...


class RandomBookInfo:
    def __init__(self, characters, locations):
        self.characters = characters
        self.locations = locations

    def rand_first_info(self)->str:
        random_character = random.choice(self.characters)
        return random_character

    def rand_second_info(self)->str:
        random_locations = random.choice(self.locations)
        return random_locations

class RandomMovieInfo:
    # No __init__ this time

    def rand_first_info(self)->str:
        movie_chars = ["Indiana Jones", "James Bond", "Han Solo", "Batman", "Ellen Ripley", "The Joker", "John McClane", "Tyler Durden", "Darth Vader", "Marty McFly"]
        random_character = random.choice(movie_chars)
        return random_character

    def rand_second_info(self)->int:
        num_list = [1, 2, 3, 4, 5, 6]
        random_number = random.choice(num_list)
        return random_number



def main():
    dune_characters = ["Paul Atreides", "Lady Jessica", "Thufir Hawat", "Duncan Idaho", "Wellington Yueh", "Leto Atreides", "Chani", "Vladimir Harkonnen", "Feyd-Rautha"]
    dune_locations = ["Arrakis", "Tleilax", "Giedi Prime", "Caladan", "Parmentier", "Poritrin", "Ix", "Salusa Secundus"]

    Dune = RandomInfo = RandomBookInfo(dune_characters, dune_locations)
    Movie = RandomInfo = RandomMovieInfo()

    print("Character: ", Dune.rand_first_info())
    print("Staring Location", Dune.rand_second_info(), "\n")
    print("Movie Character: ", Movie.rand_first_info())
    print("Roll d6: ", Movie.rand_second_info())
    


if __name__=="__main__":
    main()
    