import random

while True:
    try:
        dice_number_minimum = int(input("Enter the minimum number for the dice: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        dice_number_maximum = int(input("Enter the maximum number for the dice: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# roll 1
roll1 = random.randint(noppa_luku_minimi, noppa_luku_maksimi)
print(f"The first die shows the number: {roll1}")

# roll 2
roll2 = random.randint(noppa_luku_minimi, noppa_luku_maksimi)
print(f"The second die shows the number: {roll2}")

# quest_input
while True:
    try:
        quest_input = int(input(f"What is {roll1} + {roll2}? "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if quest_input == (roll1 + roll2):
    print("Your number is correct!")
else:
    print(f"Your number was incorrect. The correct answer would have been {roll1 + roll2}.")
# end
