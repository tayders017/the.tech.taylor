#Project overview:
#Use your Python dictionary skills to keep point totals for 4 people playing a game of scrabble!
#Say goodbye to the pencil-and-notebook scoring method of the past.
#In this project, you will process some data from a group of friends playing scrabble.
#You will use dictionaries to organize players, words, and points.
#
#
#Additional feature to add for practice:
# - play_word():
# - update_point_totals():
# - allow lowercase input to letter_to_points
#Additional features I came up with:
# - Add option to account for double/triple word scores
# - Add option to account for empty rack bonus
# - Advanced additional features: create gui of board that tracks all moves


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Combine letters and points into a dictionary
letter_to_points = {letters:points for letters, points in zip(letters, points)}
#print(letter_to_points)

#Need to account for blank tiles, add element to dictionary with key of " " and value of 0
letter_to_points[" "] = 0
print(letter_to_points)

#Create function that takes word and returns how much word is worth
def score_word(word):
  #Define point_total
  point_total = 0
  #Create loop to add the point value of each letter to point_total
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total
#Test function
#browniw_points = score_word("BROWNIE")
#print(browniw_points)

#Create dictionary to map players to a list of words they have played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#Create dictionary for player_to_points
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
#print(player_to_points)

def play_word(player, word):
  player_to_words[player].append(word)
play_word("player1", "CODE")
print(play_word)
