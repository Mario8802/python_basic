name = input()
academy_points = float(input())
number_of_jury = int(input())
total_points = academy_points
for current_grade in range(number_of_jury):
    current_jury_name = input()
    points = float(input())
    current_points = len(current_jury_name) * points / 2
    total_points += current_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {name} you need {diff:.1f} more!")