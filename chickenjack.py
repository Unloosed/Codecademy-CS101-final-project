# DESCRIPTION OF PROJECT
# -------------------------------------------------------------------
# CHICKENJACK
# Mixture of a game of Chicken and Blackjack
# As many players as you want!
# -------------------------------------------------------------------
# General info: start at 0, try to get as close to 21 as possible 
# without crossing over to 22 (or higher number)
# -------------------------------------------------------------------
# Multiplayer mode: each player takes turns making a choice--do 
# they take an increment or do they chicken out?
# If they chicken out, the other players should take increments until
# they get a higher number than the chicken(s).
# If a player's total is less than or equal to 21, they can win if they
# end up with the highest score!
# If they go over, though, they lose and the players with scores of
# 21 or less win!
# Note: ties are possible!

import random # Import random() for increment() function in Player

# Player class
class Player():
    number_of_players = 0

    def __init__(self): # Constructor
        Player.number_of_players += 1
        self.id = Player.number_of_players
        self.score = 0
        self.in_game = True

    def increment(self): # Increments Player's score and prints the result
        incremented_number = random.randint(1, 10) 
        print("Incrementing score by " + str(incremented_number) + ":\n")
        self.score += incremented_number
        print("Your new score is " + str(self.score) + ".\n")
        if (self.score > 21):
            self.lost_game()

    def lost_game(self):
        self.in_game = False
        print("Oh no! Player " + str(self.id) + 
        " has a score of " + str(self.score) + ". They are out!\n")
        Player.number_of_players -= 1 # Still need to check highest score


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
    number_of_players_selected = int(input("How many players?\n"))
else: number_of_players_selected = 1
print("\nPlayer(s): " + str(number_of_players_selected) + "\n")

# Initialize Player object(s)
players = []
for i in range(1, number_of_players_selected+1):
    players.append(Player())

# Ask to increment scores until everyone has exited the game
valid_player_increment_selection = False
while (Player.number_of_players != 0):
    for player in players:
        if (player.in_game == False):
            continue
        else:
            player_increment_selection_prompt = "Player " + str(player.id) + ", your current score is " + str(player.score) + ". Would you like to increment your score? Y/N\n"
            while (valid_player_increment_selection == False):
                player_increment_selection = input(player_increment_selection_prompt).lower()
                if ((player_increment_selection != "y") and 
                (player_increment_selection != "yes") and 
                (player_increment_selection != "n") and
                (player_increment_selection != "no")):
                    print(invalid_selection)
                else: valid_player_increment_selection = True
            if ((player_increment_selection == "y") or 
            (player_increment_selection == "yes")):
                player.increment()
                valid_player_increment_selection = False
            else: 
                player.in_game = False
                Player.number_of_players -= 1
                valid_player_increment_selection = False

# Compare scores to see who (if anyone) wins!
highest_score = -1
highest_score_player_ids = []
for player in players:
    if ((player.score > highest_score) and (player.score <= 21)):
        highest_score = player.score
        highest_score_player_ids.clear()
        highest_score_player_ids.append(player.id)
    elif (player.score == highest_score):
        highest_score_player_ids.append(player.id)
if (highest_score == -1):
    print("\nLooks like nobody won this time...")
else: print("\nWow! Player(s) " + str(highest_score_player_ids) + " won with a score of " + str(highest_score) + ". Nice job!\n")
# That's all, folks!
