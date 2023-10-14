budget = float(input())
gas = float(input())
day = input()
discount = 0
tour_guide = 100
price_for_gas = gas * 2.10


if day == "Saturday":
    discount = (price_for_gas + tour_guide) * 0.10
elif day == "Sunday":
    discount = (price_for_gas + tour_guide) * 0.20

total_sum = price_for_gas + tour_guide
final_sum = total_sum - discount
diff = abs(budget - final_sum)

if budget > final_sum:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
elif budget < final_sum:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
