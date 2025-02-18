import random

def start_game():
    print('Welcome to Number Guessing Game!')
    print('Instructions: try to guess a number between 1 and 10.')
    p_name = input('Enter your name: ').strip()
    return p_name

def get_random_number():
    return random.randint(1, 10)

def get_user_guess():
    while True:
        try:
            guess = int(input('Enter your guess: ').strip())
            if 1 <= guess <= 10:
                return guess
            else:
                print('❌ Invalid guess. Try again.')
        except ValueError:
            print('❌ Invalid input. Enter a valid number.')
            
def check_guess(guess, number):
    if guess < number:
        print('🔺 Guess higher.')
    elif guess > number:
        print('🔻 Guess lower.')
    else:
        print('🎉 Congratulations! You guessed the correct number.')
        
def end_game():
    while True:
        play_again = input('Do you want to play again? (yes/no): ').strip().lower()
        if play_again == 'yes':
            return True
        elif play_again == 'no':
            print('👋 Thank you for playing.')
            return False
        else:
            print('❌ Invalid input. Enter "yes" or "no".')
            
def main():
    player_name = start_game()
    r_number= get_random_number()
    attempts=0
    game_over=False
    while not game_over:
        attempts+=1
        user_guess = get_user_guess()
        check_guess(user_guess, r_number)
        if user_guess == r_number:
            print(f'🎉 Congratulations {player_name}! You guessed the number in {attempts} attempts.')
            break
        else:
            game_over = False
    if end_game():
        main()
    else:
        print('👋 Thank you for playing.')
if __name__ == '__main__':
    main()

    
