#1 Vad skrivs ut?
limit = 15
index = 5
while index <= limit:
    print(index)
    index = index + 2
print("**************")

#2 Vad skrivs ut?
for i in range(10):
    if i == 5:
        print(" ")
    else:
        print(i)
print("**************")

#3 Vad blir summan? Skriv ner din bästa gissning innan du kör koden.
counter = 0
for i in range(6):
    counter += i
print(counter)
print("**************")

#5 Vad skrivs ut?
# Kan du göra om koden så att den skriver ut "time" i stället?
message = "its_time_to_get_coding"
print(message[3:7])
print(message[4:8])
print("**************")

# 6 Vad skrivs ut?
# Kan du flytta linjen ett steg åt höger?
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
print("**************")

#4 Vad skrivs ut?
#För att förstå koden kan du sätta ut brytpunkter och köra med debugging.
# Det kan också underlätta att skriva samtidigt med papper och penna
x = 0
y = 1

while y < 10:
    if y % 2 == 0:
        x -= y  # sätt brytpunkt här
    else:
        x += y * y  # sätt brytpunkt här
    y += 1
print(x, y)



