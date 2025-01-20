friends = ["Sam", "Merry", "Pippin"]
friends.append("Sméagol")
print(friends)

friends = ["Sam", "Merry", "Pippin"]
length = len(friends)
print(length)    # 3

friends = ["Sam", "Merry", "Pippin"]
print(friends[0])  # Sam
print(friends[1])  # Merry

print(friends[-1])  # Pippin
print(friends[-3])  # Sam

friends = ["Sam", "Merry", "Pippin"]
friends.append("Sméagol")
friends[3] = "Gollum"     # friends[-1] fungerar också
print(friends)
# ['Sam', 'Merry', 'Pippin', 'Gollum']

x = "python"
print( x[:2] )   # py
print( x[2:5] )  # tho
print( x[4:] )   # on