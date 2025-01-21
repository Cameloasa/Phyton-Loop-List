
#3 Kvittouträknaren
# Version 1 : Gör ett program som upprepade gånger ber användaren skriva in ett tal.
#När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen.

print("Välkommen till Kvittokompis VERSION 1! Avsluta genom att skriva: quit")
# Variabel för att hålla summan av talen
total = 0

# Starta en while-loop för att läsa in belopp
while True:
    # Be användaren skriva in ett belopp
    belopp = input("Skriv in ett belopp: ")

    # Kolla om användaren vill avsluta
    if belopp.lower() in "quit":
        break

    # Försök att omvandla inmatningen till ett tal
    try:
        belopp = float(belopp)
        if belopp < 0:
            print("Negativa belopp är inte tillåtna, försök igen!")
        else:
            total += belopp
    except ValueError:
        print("Ogiltigt belopp, försök igen!")

print(f"Det blir {total} kr totalt. Välkommen åter!")
print("****************************************")

"""
Version 1 Test fal:
input : 100 output: 100
input:10,20, 15 output: 45
"""

#Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
print("Välkommen till Kvittokompis VERSION 2! Avsluta genom att skriva: quit")

# Variabel för att hålla summan av talen
total = 0

# Starta en while-loop för att läsa in antal personer
while True:

    ## Be användaren skriva in hur många personer är
    try:
        antal_personer = int(input("Hur många är ni?: "))
        if antal_personer <= 0:
            print("Antalet personer måste vara större än 0, försök igen!")
        else:
            break
    except ValueError:
        print("Ogiltigt antal personer, försök igen!")


# Starta en while-loop för att läsa in belopp
while True:
    # Be användaren skriva in ett belopp
    belopp = input("Skriv in ett belopp: ")

    # Kolla om användaren vill avsluta
    if belopp.lower() in "quit":
        break

    # Försök att omvandla inmatningen till ett tal
    try:
        belopp = float(belopp)
        if belopp < 0 :
            print("Negativa belopp är inte tillåtna, försök igen!")
        else:
            total += belopp

    except ValueError:
        print("Ogiltigt belopp, försök igen!")

# Räkna ut och skriv ut resultatet
if total > 0:
    per_person = total / antal_personer
    print(f"Det blir {total} kr totalt, alltså {per_person:.2f} kr per person. Välkommen åter!")
else:
    print("Inga belopp angavs. Välkommen åter!")

print("****************************************")

"""
Version 2 Test fal:
100, 1 person,100
100, 2 personer, 50
10, 10, 40 personer, 20, 0.5
30, 20, 30, 1 person, 80, 80
"""
# Version 3: programmet ska fråga hur många procent dricks man vill lägga på.
# Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.

print("Välkommen till Kvittokompis VERSION 3! Avsluta genom att skriva: quit")

# Variabel för att hålla summan av talen
total = 0

# Be användaren ange hur många personer de är
while True:
    try:
        antal_personer = int(input("Hur många är ni?: "))
        if antal_personer <= 0:
            print("Antalet personer måste vara större än 0, försök igen!")
        else:
            break
    except ValueError:
        print("Ogiltigt antal personer, försök igen!")

# Be användaren ange dricks procent
dricks_input = input("Hur många procent dricks vill ni lägga? (tryck Enter för 10%): ")
if dricks_input.strip() == "":
    dricks_procent = 10  # Standardvärde
else:
    try:
        dricks_procent = float(dricks_input)
        if dricks_procent < 0:
            print("Dricks procent kan inte vara negativ. Använder standardvärde (10%).")
            dricks_procent = 10
    except ValueError:
        print("Ogiltig inmatning. Använder standardvärde (10%).")
        dricks_procent = 10

# Starta en while-loop för att läsa in belopp
while True:
    # Be användaren skriva in ett belopp
    belopp = input("Skriv in ett belopp: ")

    # Kolla om användaren vill avsluta
    if belopp.lower() == "quit":
        break

    # Försök att omvandla inmatningen till ett tal
    try:
        belopp = float(belopp)
        if belopp < 0:
            print("Negativa belopp är inte tillåtna, försök igen!")
        else:
            total += belopp  # Lägg till beloppet till totalen
    except ValueError:
        print("Ogiltigt belopp, försök igen!")

# Beräkna dricks belopp och totalsumma
dricks_belopp = total * (dricks_procent / 100)
total_with_tip = total + dricks_belopp

# Räkna ut kostnad per person
if total > 0:
    per_person = total_with_tip / antal_personer
    print(f"\nDet blir {total_with_tip:.2f} kr totalt, inklusive {dricks_procent}% dricks.")
    print(f"Det blir {per_person:.2f} kr per person. Välkommen åter!")
else:
    print("\nInga belopp angavs. Välkommen åter!")

"""
Version 2 Test fal:
100, 1 person, 10%, 110, 55
100, 2 personer, 15%, 115, 57.50
10, 10, 40 personer, 100%. 40, 1
30, 20, 30, 1 person, 20%, 96, 96
"""
