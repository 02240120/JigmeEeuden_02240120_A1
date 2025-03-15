#Guess the number
import random

def guess_number_game():
    print("\n ____guessing game___")
    number_to_guess = random.randint(1, 20)
    while True:
        user_guess = int(input("Guess a number between 1 and 20: "))
        if user_guess < number_to_guess:
            print("Higher!")
        elif user_guess > number_to_guess:
            print("Lower!")
        else:
            print("Correct! You've guessed the number.")
            break

#Rock, Paper, Scissors


def rock_paper_scissors():
    


    while True:
        choices=['rock','paper','scissor']
        
        user_choice = input("Your choice: ").lower()
        computer_choice=random.choice(choices)
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        
        
        print(f"Computer chose: {computer_choice}")


        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            break
        else:
            print("You lose!")
            break




def main():
    while True:
        print("\n__game menu__")
        print('1.guessing game')
        print('2.rock, paper, scissors')
        print('3.exiting...')
        
        choose=input('enter your choice(1-3):')
        if choose=='1':
            guess_number_game()
        elif choose=='2':
            rock_paper_scissors()
        elif choose=='3':
            print('exiting...')
            break
        else:
            print('invalid.please enter 1-3')
if __name__ == "__main__":
    main()


            