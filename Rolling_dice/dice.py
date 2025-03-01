import random
def start_simulation():
    print('Rolling dice simulation started')
    print('Enter no of dice and no of sides on dice to roll')
    
def get_user_input():
    while True:
        try:
            no_of_dice = int(input('Enter no of dice: '))
            no_of_sides = int(input('Enter no of sides on dice: '))
            if no_of_dice < 1 or no_of_sides < 2:
                print('No of dice should be greater than 0 and no of sides should be greater than 1')
                return get_user_input()
            else:
                return no_of_dice, no_of_sides
        except ValueError:
            print('Enter valid input')
            return get_user_input()
def roll_dice(no_of_dice, no_of_sides):
    rolls=[random.randint(1,no_of_sides) for _ in range(no_of_dice)]
    return rolls

def display_result(rolls):
    print(' You Rolled:', rolls)
    print('Total:', sum(rolls))
    
def statistical_analysis(rolls):
    freqyence={i:rolls.count(i) for i in rolls}
    print('Frequency of each element: ', freqyence)
    print('Average: ', sum(rolls)/len(rolls))
    print('Max: ', max(rolls))
    print('Min: ', min(rolls))
    print('Count: ', len(rolls))
    
def replay():
    while True:
        replay = input('Do you want to roll again? (y/n): ')
        if replay.lower() == 'y':
            return True
        elif replay.lower() == 'n':
            return False
        else:
            print('Enter valid input')
            
def main():
    start_simulation()
    while True:
        no_of_dice, no_of_sides = get_user_input()
        rolls = roll_dice(no_of_dice, no_of_sides)
        display_result(rolls)
        statistical_analysis(rolls)
        if not replay():
            break
    print('Rolling dice simulation ended')

if __name__ == '__main__':
    main()