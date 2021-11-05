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

    # def computer(self, player):

    #     bot= random.choice(["rock", "paper", "scissors"])
    #     result = None

    #     if player.choice == "paper" and bot == "rock":
    #         result = player
    #     elif player.choice == "rock" and bot == "paper":
    #         result = bot
    #     elif player.choice == "scissors" and bot == "paper":
    #         result = player
    #     elif player.choice == "paper" and bot == "scissors":
    #         result = bot
    #     elif player.choice == "rock" and bot == "scissors":
    #         result = player
    #     elif player.choice == "scissors" and bot == "rock":
    #         result = bot

    #     return result

        
            

    
        
            