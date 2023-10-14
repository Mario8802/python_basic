budget = float(input())
nights = int(input())
price_per_night = int(input())
percent_extra_cost = int(input())
discount = 0
if nights > 7:
    discount = price_per_night * 0.05
    price_per_night = price_per_night - discount
sum_extra_cost = (budget * percent_extra_cost) / 100

total_sum = (nights * price_per_night) + sum_extra_cost
diff = abs(budget - total_sum)
if total_sum < budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
if budget < total_sum:
    print(f"{diff:.2f} leva needed.")
