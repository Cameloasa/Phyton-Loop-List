
# version 1
import random

lowest_number = 1
highest_number = 100
secret = random.randint(lowest_number, highest_number)
antal_gissningar = 0

print(f"Välkommen till gissa talet!\nJag tänker på ett tal mellan {lowest_number} och {highest_number}.\nKan du gissa vilket det är?")

while True:
    gissning = input("Gissa: ")

    try:

        gissning = int(gissning)
        antal_gissningar += 1

        if gissning < lowest_number or gissning > highest_number:
            print(f"Nej, det är ogiltig nummer!\nDu måste välja mellan {lowest_number} och {highest_number}!\nFörsök igen!")
        elif gissning < secret:
            print("Nej, det är för lågt!")
        elif gissning > secret:
            print("Nej, det är för högt!")
        elif gissning == secret:
            print(f"Det är rätt!! Du gjorde det på {antal_gissningar} gissningar.")
            break
    except ValueError:
        print("Var snäll och skriv in ett giltigt heltal.")

print("*******************************")

# Version 2

lowest_number = 1
highest_number = 100
secret = random.randint(lowest_number, highest_number)
antal_gissningar = 0

print(
    f"Välkommen till gissa talet!\nJag tänker på ett tal mellan {lowest_number} och {highest_number}.\nKan du gissa vilket det är?")

while True:
    gissning = input("Gissa: ")

    try:

        gissning = int(gissning)
        antal_gissningar += 1

        if gissning < lowest_number or gissning > highest_number:
            print(
                f"Nej, det är ogiltig nummer!\nDu måste välja mellan {lowest_number} och {highest_number}!\nFörsök igen!")
        elif abs(gissning - secret) <= 5 and gissning != secret:
            if gissning < secret:
                print("Nu börjar det brännas! Det är dock fortfarande för lågt!")
            else:
                print("Nu börjar det brännas! Det är dock fortfarande för högt!")
        elif gissning < secret:
            print("Nej, det är för lågt!")
        elif gissning > secret:
            print("Nej, det är för högt!")
        elif gissning == secret:
            print(f"Det är rätt!! Du gjorde det på {antal_gissningar} gissningar.")
            break
    except ValueError:
        print("Var snäll och skriv in ett giltigt heltal.")



