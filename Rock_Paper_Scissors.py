import random

class RPSGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'

    def display_result(self, user_choice, computer_choice, winner):
        print(f"\nYour choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
            self.user_score += 1
        else:
            print("Computer wins!")
            self.computer_score += 1
        print(f"Score - You: {self.user_score}, Computer: {self.computer_score}\n")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == 'yes'

def print_instructions():
    print("\nWelcome to Rock-Paper-Scissors Game!")
    print("Instructions:")
    print("Rock beats scissors, scissors beat paper, and paper beats rock.")
    print("You and the computer will each choose one of these options.")
    print("Let's see who wins! Enjoy the game!\n")

def main():
    print_instructions()
    
    game = RPSGame()

    while True:
        user_choice = game.get_user_choice()
        computer_choice = game.get_computer_choice()

        winner = game.determine_winner(user_choice, computer_choice)
        game.display_result(user_choice, computer_choice, winner)

        if not game.play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
