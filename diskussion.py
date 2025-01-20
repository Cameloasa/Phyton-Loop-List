#1 Vad skrivs ut?
limit = 15
index = 5
while index <= limit:
    print(index)
    index = index + 2
print("**************")
"""
start = 5
stop = 15
step = 2
output : 5, 7, 9, 11, 13, 15
"""

#2 Vad skrivs ut?
for i in range(10):
    if i == 5:
        print(" ")
    else:
        print(i)
print("**************")
"""
start = 0
stop = 9
step = 1
jump over 5
output : 0,1,2,3,4,6,7,8,9
"""

#3 Vad blir summan? Skriv ner din bästa gissning innan du kör koden.
counter = 0
for i in range(6):
    counter += i
print(counter)
print("**************")
"""
start = 0
stop = 5
step = 1
output : 0+1+2+3+4+5 = 15
"""

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

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y + 1:  # Flytta linjen ett steg åt höger
            s += "#"
        else:
            s += "."
    print(s)
print("**************")



