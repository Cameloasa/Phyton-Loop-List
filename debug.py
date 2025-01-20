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

"""
x
start = 0
stop = ?

y 
start = 1
stop = 9

Iteration:
y = 1 (odd):

x += y * y → x = 0 + 1 * 1 = 1
y += 1 → y = 2

y = 2 (even):

x -= y → x = 1 - 2 = -1
y += 1 → y = 3

y = 3 (odd):

x += y * y → x = -1 + 3 * 3 = -1 + 9 = 8
y += 1 → y = 4

y = 4 (even):

x -= y → x = 8 - 4 = 4
y += 1 → y = 5

y = 5 (odd):

x += y * y → x = 4 + 5 * 5 = 4 + 25 = 29
y += 1 → y = 6

y = 6 (even):

x -= y → x = 29 - 6 = 23
y += 1 → y = 7

y = 7 (odd):

x += y * y → x = 23 + 7 * 7 = 23 + 49 = 72
y += 1 → y = 8

y = 8 (even):

x -= y → x = 72 - 8 = 64
y += 1 → y = 9

y = 9 (odd):

x += y * y → x = 64 + 9 * 9 = 64 + 81 = 145
y += 1 → y = 10

"""

x = 0

#for loop iteration 1 to 9 (inclusive)
for y in range(1, 10):
    if y % 2 == 0:
        x -= y  #
    else:
        x += y * y  #

print(x, y)