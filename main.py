#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

########################
def check_number(user_guess , computer_guess, turns):
 if user_guess > computer_guess:
   print("Your Guess is Too high.")
   return turns - 1
 elif user_guess < computer_guess:
   print("Your Guess is Too low")
   return turns - 1
 else:
   print(f"You have guess the Correct answer. The Correct answer is {computer_guess}")

########################
def set_difficulty():
  difficulty = input("Which difficulty would you like to take. Type 'easy' for Easy difficulty and 'hard' for Hard difficulty : ").lower()
  
  if difficulty == 'easy':
    number_of_turns = 10
  elif difficulty == 'hard':
    number_of_turns = 5
  else:
    print("You have type the wrong the word.")
  return number_of_turns

########################
def game():
  computer_guess = random.randint(1,100)
  user_guess = 0
  print(f"computer gues : {computer_guess}")
  turns = 0
  turns = set_difficulty()
  while user_guess != computer_guess:
    print(f"You have {turns} turns for guessing the number")
    user_guess = int(input("Enter your Guess number : "))
    turns = check_number(user_guess, computer_guess, turns)
    if turns == 0:
      print("You have lost the game.")
      return

      
###### MAIN CODE ######
print("Welcome to Guess Number Game.\nRules :\n1.There are two level 'Easy' which gives 10 turns to guess the number and 'Hard' which gives only 5 turns to guess the number.\n2.You need to guess number in between 1 to 100.\n3.Lastly Enjoy the Game.")
game()
  
  
