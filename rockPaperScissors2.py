# CS10 - M12 Assignment: Rock-Paper-Scissors Program
# LETICIA NARDI
# output samples are in the end of the file.

import random

run_again = True

while run_again == True:
 
 print("\nMake your throw")
 player_move = str(input(" Type rock, paper or scissors: ")).lower()

 # Defining numbers to game options
 computer_move = random.randint(1,3)  # computer_move will be 1, 2, or 3

 if computer_move == 1:
  computer_move = "rock"
 elif computer_move == 2:
  computer_move = "paper"
 elif computer_move == 3:
  computer_move = "scissors"
 
 # print(f"computer move was: {computer_move}")


 # playing the game
 if player_move == computer_move:
  print(f"Tie! You both chose {player_move}.")

 # ROCK loses to paper // wins scissors
 elif player_move == "rock":
  if computer_move == "paper":
   print(f"\nYou lose! {player_move} can't beat {computer_move}.")
  else:
   print(f"\nYou win! {player_move} beats {computer_move}.")

 # PAPER loses to scissors // wins rock
 elif player_move == "paper":
  if computer_move == "scissors":
   print(f"\nYou lose! {player_move} can't beat {computer_move}.")
  else:
   print(f"\nYou win! {player_move} beats {computer_move}.")

 # SCISSORS loses to rock // wins paper
 elif player_move == "scissors" or "scissor":
  if computer_move == "rock":
   print(f"\nYou lose! {player_move} can't beat {computer_move}.")
  else:
   print(f"\nYou win! {player_move} beats {computer_move}.")

 # invalid options
 else:
   print(f"\n{player_move} is either misspelled or invalid.")
  
  
 # play again
 again = input("\n Keep playing? (y/n) ")
 if again.lower() == "n":
  run_again = False
 elif again.lower() == "y":
  run_again = True
 else:
  run_again = True
  print("\nWe assumed yes. \nLet's do it again. :)")
  
  
print("\nBye")



#########################################################

### OUTPUTS 1: ###

# $ python -u "c:\Users\letic\Desktop\hello\rockPaperScissors2.py"

# Make your throw
#  Type rock, paper or scissors: paper

# You win! paper beats rock.

#  Keep playing? (y/n) n

# Bye

#########################################################

### OUTPUTS 2: ###

# $ python -u "c:\Users\letic\Desktop\hello\rockPaperScissors2.py"

# Make your throw
#  Type rock, paper or scissors: rock

# You win! rock beats scissors.

#  Keep playing? (y/n) n

# Bye

#########################################################

### OUTPUTS 3: ###

# You win! paper beats rock.

#  Keep playing? (y/n) y

# Make your throw
#  Type rock, paper or scissors: scissors

# You win! scissors beats paper.

#  Keep playing? (y/n) n

# Bye