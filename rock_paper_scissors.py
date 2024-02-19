# Rock Paper Scissors Game
import random

print('''
Welcome to "Rock-Paper-Scissors Game"
      
Instructions:
      Enter your choice in small letters without any special character
      You can choose either to play another round or not
      Winner will be announced at the end of each round

Let's play together!!!
''')

def get_user_choice():
    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\n It's a tie! \n"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "\n You win! \n"
    else:
        return "\n Computer wins! \n"
    
def play():
    user_score = 0
    computer_score = 0
    while True:
        print("\n--- New Round ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("\nYour choice:", user_choice)
        print("Computer's choice:", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "\n You win! \n":
            user_score += 1
        elif result == "\n Computer wins! \n":
            computer_score += 1
        
        print("Scoreboard - You:", user_score, "Computer:", computer_score)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

play()