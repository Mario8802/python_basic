team = input()
games = int(input())
points = 0
win_counter = 0
draw_counter = 0
lose_counter = 0
for _ in range(games + 1):
    result = input()
    if result == "W":
        points += 3
        win_counter += 1
    elif result == "D":
        points += 1
        draw_counter += 1
    elif result == "L":
        points += 0
        lose_counter += 1
#win_rate = win_counter / games * 100
if games == 0:
    print(f"{team} hasn't played any games during this season.")
else:
    win_rate = win_counter / games * 100
    print(f"{team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {win_counter}")
    print(f"## D: {draw_counter}")
    print(f"## L: {lose_counter}")
    print(f"Win rate: {win_rate:.2f}%")