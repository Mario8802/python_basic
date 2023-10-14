budget = float(input())
season = input()
destination = ''
total_sum = 0
place = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        total_sum = budget * 0.30
        place = 'Camp'
    elif season == 'winter':
        total_sum = budget * 0.70
        place = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        total_sum = budget * 0.40
        place = 'Camp'
    elif season == 'winter':
        total_sum = budget * 0.80
        place = 'Hotel'
else:
    destination = 'Europe'
    total_sum = budget * 0.90
    place = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{place} - {total_sum:.2f}")