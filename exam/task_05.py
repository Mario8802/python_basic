import sys
from sys import maxsize


player = input()

goals_count = int(input())
count_goals = 0
best_player = ""
top_goals = - sys.maxsize
while True:
    player = input()
    goals_count = int(input())
    count_goals += goals_count
    if goals_count >= 3:
        best_player == player
        print(f"{player} is the best player!")
        print(f"He has scored {goals_count} goals and made a hat trick!!!")

    if goals_count < 3:
        print(f"He has scored {goals_count} goals")

    if player == "END":
        break


