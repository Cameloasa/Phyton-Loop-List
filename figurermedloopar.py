"""

a-f

g-j

"""

"""
x
start = 1
stop = 8

y 
start = 1
stop = 6

Det här programmet skriver ut en "diagonal linje" av #-tecken på en matris av storlek 6x8. 
Linjen börjar i det övre vänstra hörnet och går snett nedåt åt höger, med varje rad tryckt på en ny rad. 
Varje # ersätter punkten (.) i den aktuella raden.
"""
#4 Figurer med loopar
#Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
# a
for y in range(1, 7): # Iterera över rader
    s = ""
    for x in range(1, 9):  # Iterera över kolumner
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

# b
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

# c
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x in [3, 4, 5]:
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

# d
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3:
            s += "#"
        elif y == 3:
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

# e
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y == 1 and 5 <= x <= 6:
            s += "#"
        elif y == 2 and  x == 5:
            s += "#"
        elif y == 3 and 4 <= x <= 5:
            s += "#"
        elif y == 4  and (x == 3 or x == 5):
            s += "#"
        elif y == 5 and (x == 2 or x == 5):
            s += "#"
        elif y == 6 and (x == 1 or x == 5):
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

# f
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y == 1 and (x == 1 or x == 6):
            s += "#"
        elif y == 2 and  (x == 2 or x == 5):
            s += "#"
        elif y == 3 and 3 <= x <= 4:
            s += "#"
        elif y == 4  and 3 <= x <= 4:
            s += "#"
        elif y == 5 and (x == 2 or x == 5):
            s += "#"
        elif y == 6 and (x == 1 or x == 6):
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

# g
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x % 2 == 1:
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

# h
for y in range(1, 7):
    s = ""
    for x in range(1, 9):  # Iterera över kolumner
        if y == 2 and 2 <= x <= 7 :
            s += "#"
        elif y == 3 and (x == 2 or x == 7):
            s += "#"
        elif y == 4 and (x == 2 or x == 7):
            s += "#"
        elif x == 5 and 2 <= x <= 7 :
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

# j
for y in range(1, 7):
    s = ""
    for x in range(1, 9):  # Iterera över kolumner
        if y == 1 and (x == 3 or x == 6):
            s += "#"
        elif y == 2 and (x == 3 or x == 6):
            s += "#"
        elif y == 3 and (x == 3 or x == 6):
            s += "#"
        elif y == 5 and x % 2 != 1:
            s += "#"
        elif y == 6 and x % 2 == 1:
            s += "#"
        else:
            s += "."
    print(s)
print("**************")


# i
for y in range(1, 7):  # Iterera över rader
    s = ""
    for x in range(1, 9):  # Iterera över kolumner (1 till 8)
        if (x - y) % 3 == 1:  # Första mönstret: #
            s += "#"
        elif (x - y) % 3 == 2:  # Andra mönstret: O
            s += "O"
        else:  # Resten är .
            s += "."
    print(s)
print("**************")

# Version 2 av i
# De tre unika raderna
lines = [
    ".#O.#O.#",  # Rad 1
    "O.#O.#O.",  # Rad 2
    "#O.#O.#O"   # Rad 3
]

# Skriv ut raderna två gånger
for i in range(2):  # Upprepa två gånger
    for line in lines:
        print(line)
print("**************")