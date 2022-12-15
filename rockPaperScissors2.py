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

#  elif player_move != "rock" and player_move != "paper" and player_move != "scissors" an player_move != "scissor": 
#    print(f"\n{player_move} is either misspelled or invalid.")
   
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

