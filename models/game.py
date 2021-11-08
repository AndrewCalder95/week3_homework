from models.player import *
import random

class Game:
    def __init__(self):
        self

    def play_game(self, player_1, player_2):

        result = None

        if player_1.choice == "paper" and player_2.choice == "rock":
            result = player_1
        elif player_1.choice == "rock" and player_2.choice == "paper":
            result = player_2
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            result = player_1
        elif player_1.choice == "paper" and player_2.choice == "scissors":
            result = player_2
        elif player_1.choice == "rock" and player_2.choice == "scissors":
            result = player_1
        elif player_1.choice == "scissors" and player_2.choice == "rock":
            result = player_2

        return result


        
            

    
        
            