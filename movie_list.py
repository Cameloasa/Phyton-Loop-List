
#1a Skriv färdigt kodexemplet.
answer = 0
for i in range(11): # (0-11)
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

#1b Räkna ut summan av alla tal mellan 1 och 100.
#(inklusive 1 och 100, rätt svar ska bli 5050)
answer = 0
for number in range (101):
    answer = answer + number
print("Summan av talen 1 till 100 är: " + str(answer))

#1c Skriv om 1b så att den använder en while-loop.
number = 0
answer = 0
while number <= 100:
    answer = answer + number
    number = number + 1
print("Summan av talen mellan 1 till 100 ar: " + str(answer))

#2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
numbers = [1, -2, 3, -2, 4, -3]
answer = 0
for number in numbers:
    answer = answer + number
print(f"Summan av talen i listan är: {answer}")

#3 Träna på att skapa och manipulera listor.
#Alla uppgifter ska lösas med funktionerna som står i presentationen.

#3a Skapa en lista med namnen på fyra filmer.
#Namnen ska vara strängar.
#Skriv ut hela listan med funktionen print.

movies = [
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Return of the King",
    "An Unexpected Journey"
]

print("'The Lord of the Rings' and 'The Hobbit' film series, directed by Peter Jackson are:")
for movie in movies:
    print(movie)

# 3b Lägg till "The Hobbit: The Desolation of Smaug (2013)" sist i listan
movies.append("The Desolation of Smaug")
print("\nAfter adding 'The Hobbit: The Desolation of Smaug':")
for movie in movies:
    print(movie)

# 3c Lägg till "The Hobbit: The Battle of the Five Armies (2014)" på första platsen i listan
movies.insert(0, "The Battle of the Five Armies")
print("\nAfter adding 'The Hobbit: The Battle of the Five Armies (2014)' to the first position:")
for movie in movies:
    print(movie)

#3d Ta reda på vilken position (index) "Fellowship of the ring" har nu. index()
print("\nThe index of The Fellowship of the Ring")
print(movies.index("The Fellowship of the Ring"))

#3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
movies.remove("The Battle of the Five Armies")
print("\nAfter removing 'The Hobbit: The Battle of the Five Armies (2014)' to the first position")
print(movies.index("The Fellowship of the Ring"))

#3f Ta reda på hur lång listan är. (len)
print("\nThe length of my list are:")
print(len(movies))

#3g Vänd listan baklänges. reverse()
print("\n'The Lord of the Rings' and 'The Hobbit' film series, directed by Peter Jackson are:")
for movie in movies:
    print(movie)

movies.reverse()
print("\n'The Lord of the Rings' and 'The Hobbit' film series,reversed list:")
for movie in movies:
    print(movie)

#3h Sortera listan stigande i bokstavsordning.
movies.sort()
print("\n'The Lord of the Rings' and 'The Hobbit' film series,sorted list:")
for movie in movies:
    print(movie)

