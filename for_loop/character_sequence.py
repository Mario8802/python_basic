name = "Mario"
# for index in range(0, len(name)):
#     print(f"Index = {index}, symbol = {name[index]}")
#
# for charecter in name:
#     print(charecter)


# for index, character in enumerate(name):
#     print(f'Index = {index}, symbol = {character}')
some_string = input()
bonus_points = 0
for character in some_string:
    if character == "a":
        bonus_points += 1
    elif character == "e":
        bonus_points += 2
    elif character == "i":
        bonus_points += 3
    elif character == "o":
        bonus_points += 4
    elif character == "u":
        bonus_points += 5
print(bonus_points)
