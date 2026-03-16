#Simulate the Dice Game of Craps
import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)
10

def display_dice(dice):
    """Display the face values of the rolled dice."""
    die1, die2 = dice
    print(f"You rolled: {dice[0]} and {dice[1]} (Total: {sum(dice)})")

die_values = roll_dice()
display_dice(die_values)    

# Determine the outcome of the game based on the rules of Craps
sum_of_dice = sum(die_values)
if sum_of_dice in (7, 11):
    game_status = "win"
elif sum_of_dice in (2, 3, 12):
    game_status = "lose"
else:
    game_status = "continue"
    my_point = sum_of_dice
    print(f"Point is set to: {my_point}")

# Continue rolling until the player wins by rolling the point again or loses by rolling a 7
while game_status == "continue":
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:
        game_status = "win"
    elif sum_of_dice == 7:
        game_status = "lose"
# Display the final outcome of the game
if game_status == "win":
    print("Congratulations! You win!")
else:
    print("Sorry, you lose. Better luck next time!")
