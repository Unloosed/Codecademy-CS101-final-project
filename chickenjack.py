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

    def __init__(self, score=0):
        Player.number_of_players += 1
        self.player_id = Player.number_of_players
        self.score = score

greeting = "Hello! Welcome to Chickenjack!\n"
description = """This is a mixture of a game of Chicken and Blackjack.\n
The general rules of the game are as follows:\n
""" # description in progress
print(greeting)
print(description)
