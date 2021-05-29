# DESCRIPTION OF PROJECT
# ------------------------------------------------------------------------
# CHICKENJACK
# Mixture of a game of Chicken and Blackjack
# 2-player or 1-player (possibly customizable number of players?)
# ------------------------------------------------------------------------
# General info: start at 0, try to get as close to 21 as possible 
# without crossing over to 22 (or higher number)
# ------------------------------------------------------------------------
# 2-player/multiplayer mode: each player takes turns making a choice--do 
# they take an increment or do they chicken out?
# If they chicken out, the other player has to take increments until
# they get a higher number than the chicken.
# If this other player's total is less than or equal to 21, they win!
# If they go over, though, they lose and the chicken wins!
# ------------------------------------------------------------------------
# 1-player/singleplayer mode: ehhh maybe I shouldn't have a singleplayer
# mode. If there is one, the player takes increments until they chicken
# out and their score is recorded. They try to get a high score as close
# to 21 as possible, but if they go over, their record is destroyed
# and they have to start over.

import random # Import random() for increment() function in Player

# ChickenJack and Player classes
class ChickenJack:
    def __init__(self):
        self.number_of_players = 0


class Player(ChickenJack):
    single_player_mode = False
    in_game = True

    def __init__(self, score=0):
        ChickenJack.number_of_players += 1
        self.player_id = ChickenJack.number_of_players
        self.score = score

    def increment(self):
        self.score += int(random() * 10)
        if (self.score > 21):
            self.lost_game()

    def lost_game(self):
        self.in_game = False
        print("Oh no! Player " + str(self.player_id) + 
        " has a score of " + str(self.score) + ". They are out!\n")
        if (number_of_players == 1):
            print("You lost!\n")


greeting = "Hello! Welcome to Chickenjack!\n"
description = """This is a mixture of a game of Chicken and Blackjack.\n
The general rules of the game are as follows:\n
Each player starts at 0, and they try to get as close to 21 as possible 
without crossing over to 22 (or a higher number).\n
You either accept another increment to your score, or you 'chicken' out. 
After your turn, the next player does the same.\n
Each increment can be an integer between 1 and 10, inclusive.\n
Whoever has the closest score to 21 without crossing over to 22 or higher 
wins!\n"""
mode_prompt = "Do you want to play in singleplayer or multiplayer mode? S/M\n"
invalid_selection = "Invalid selection. Please try again:\n"
valid_selection_bool = False

# Print greeting and description/rules of the game to the player
print(greeting)
print(description)

# Ask for singleplayer or multiplayer mode:
while (valid_selection_bool == False):
    mode_selection = input(mode_prompt).lower()
    if ((mode_selection != "s") and  (mode_selection != "singleplayer") 
    and (mode_selection != "single") and (mode_selection != "m") 
    and (mode_selection != "multiplayer") and (mode_selection != "multi")):
        print(invalid_selection)
    else: valid_selection_bool = True
if ((mode_selection == "s") or  
    (mode_selection == "singleplayer") or (mode_selection == "single")):
    mode_selection = "Singleplayer"
else: mode_selection = "Multiplayer"
print("\nMode selection: " + mode_selection + "\n")

# Set number of players
if (mode_selection == "Multiplayer"):
    number_of_players = int(input("How many players?\n"))
else: number_of_players = 1
print("\nPlayer(s): " + str(number_of_players) + "\n")

# Initialize ChickenJack and Player objects
