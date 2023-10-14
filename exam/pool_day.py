people_count = int(input())
entry_tax = float(input())
sun_lounger = float(input())
price_for_umbrella = float(input())

from math import ceil

total_people_entry_tax = (people_count * entry_tax)
people_with_sun_lounger = ceil(people_count * 0.75) * sun_lounger
people_with_umbrella = ceil(people_count / 2 ) * price_for_umbrella

total_sum = total_people_entry_tax + people_with_sun_lounger + people_with_umbrella
print(f"{total_sum:.2f}")