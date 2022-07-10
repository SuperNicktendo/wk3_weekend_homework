from models.game import *
from models.player import Player

choice = ["Rock", "Paper", "Scissors"]

def play_game(player1, player2):
        if player1 == choice[0] and player2 == choice[2]:
            return "Player 1 wins! Rock beats scissors!"
        elif player1 == choice[1] and player2 == choice[0]:
            return "Player 1 wins! Paper beats rock!"
        elif player1 == choice[2] and player2 == choice[1]:
            return "Player 1 wins! Scissors beats paper!"
        elif player2 == choice[0] and player1 == choice[2]:
            return "Player 2 wins! Rock beats scissors!"
        elif player2 == choice[1] and player1 == choice[0]:
            return "Player 2 wins! Paper beats rock!"
        elif player2 == choice[2] and player1 == choice[1]:
            return "Player 2 wins! Scissors beats paper!"
        elif player1 == choice[0] and player2 == choice[0]:
            return None
        elif player1 == choice[1] and player2 == choice[1]:
            return None
        elif player1 == choice[2] and player2 == choice[2]:
            return None
        