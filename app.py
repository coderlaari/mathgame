import random

noppa_luku_minimi = int(input("Anna noppien minimi numero: "))
noppa_luku_maksimi = int(input("Anna noppien maksimi numero: "))

# roll 1
roll1 = random.randint(noppa_luku_minimi, noppa_luku_maksimi)
print(f"Ensimmäinen noppa näyttää luvun: {roll1}")

# roll 2
roll2 = random.randint(noppa_luku_minimi, noppa_luku_maksimi)
print(f"Toinen noppa näyttää luvun: {roll2}")

# quest_input
while True:
    try:
        quest_input = int(input(f"Mikä on {roll1} + {roll2}? "))
        break
    except ValueError:
        print("Virheellinen syöte. Anna kelvollinen numero.")

if quest_input == (roll1 + roll2):
    print("Sinun numero on oikein!")
else:
    print(f"Sinun numerosi oli väärin. Oikea vastaus olisi ollut {roll1 + roll2}.")
# loppu
