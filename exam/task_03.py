word = input()
points = 0
for letter in word:
    if letter == "a":
        points += 3
    elif letter == "i":
        points += 3
print(points)