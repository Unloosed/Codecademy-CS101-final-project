# DESCRIPTION OF PROJECT
# ---------------------------------------------------------------------------------------------------
# CHICKENJACK
# Mixture of a game of Chicken and Blackjack
# 2-player or 1-player (possibly customizable number of players?)
# ---------------------------------------------------------------------------------------------------
# General info: start at 0, try to get as close to 21 as possible 
# without crossing over to 22 (or higher number)
# ---------------------------------------------------------------------------------------------------
# 2-player/multiplayer mode: each player takes turns making a choice--do 
# they take an increment or do they chicken out?
# If they chicken out, the other player has to take increments until
# they get a higher number than the chicken.
# If this other player's total is less than or equal to 21, they win!
# If they go over, though, they lose and the chicken wins!
# ---------------------------------------------------------------------------------------------------
# 1-player/singleplayer mode: ehhh maybe I shouldn't have a singleplayer
# mode. If there is one, the player takes increments until they chicken
# out and their score is recorded. They try to get a high score as close
# to 21 as possible, but if they go over, their record is destroyed
# and they have to start over.

# Create Player class
class Player:
    number_of_players = 0
    single_player_mode = False

    def __init__(self, score=0):
        Player.number_of_players += 1
        self.player_id = Player.number_of_players
        self.score = score

greeting = "Hello! Welcome to Chickenjack!\n"
description = """This is a mixture of a game of Chicken and Blackjack.\n
The general rules of the game are as follows:\n
Each player starts at 0, and they try to get as close to 21 as possible 
without crossing over to 22 (or a higher number).\n
You either accept another increment to your score, or you 'chicken' out. 
After your turn, the next player does the same.\n
Whoever has the closest score to 21 without crossing over to 22 or higher 
wins!\n""" # description in progress
mode_prompt = "Do you want to play in singleplayer or multiplayer mode? S/M\n"
invalid_selection = "Invalid selection. Please try again:\n"
valid_selection_bool = False
# Print greeting and description/rules of the game to the player
print(greeting)
print(description)
# Ask for singleplayer or multiplayer mode:
while (valid_selection_bool == False):
    mode_selection = input(mode_prompt)
    if ((mode_selection != "S") and (mode_selection != "Singleplayer") and 
    (mode_selection != "singleplayer") and (mode_selection != "Single") and 
    (mode_selection != "single") and (mode_selection != "M") and (mode_selection 
    != "Multiplayer") and (mode_selection != "multiplayer") and (mode_selection 
    != "Multi") and (mode_selection != "multi")):
        print(invalid_selection)
    else: valid_selection_bool = True
if ((mode_selection == "S") or (mode_selection == "Singleplayer") or 
    (mode_selection == "singleplayer") or (mode_selection == "Single") or 
    (mode_selection == "single")):
    mode_selection = "S"
else: mode_selection = "M"
print("\nMode selection: " + mode_selection + "\n")
