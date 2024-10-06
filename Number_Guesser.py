import random

random_number = random.randint(0, 100)

player_choice = 0



while player_choice != random_number:

    player_choice = input("Guess the number from 0 to 100 ")

    if player_choice.isdigit():
        player_choice = int(player_choice)
    else:
        print("Pick a number next time")
        quit()

    if player_choice < random_number:
        print("Pick a higher number!")
    elif player_choice > random_number:
        print("Pick a lower number!")

print("YOU GUESSED!")
print(f"The number was {random_number}")
quit()