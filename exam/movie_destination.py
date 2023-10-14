budget = float(input())
destination = input()
season = input()
count_days = int(input())
price = 0
tax = 0
tax_to_pay = 0

if destination == "Dubai" and season == "Winter":
    price = 45000 * count_days
    tax = price * 0.30
elif destination == "Dubai" and season == "Summer":
    price = 40000 * count_days
    tax = price * 0.30

if destination == "Sofia" and season == "Winter":
    price = 17000 * count_days
    tax_to_pay = price * 0.25
elif destination == "Sofia" and season == "Summer":
    price = 12500 * count_days
    tax_to_pay = price * 0.25

if destination == "London" and season == "Winter":
    price = 24000 * count_days

elif destination == "London" and season == "Summer":
    price = 20250 * count_days

total_sum = price + tax_to_pay - tax
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
elif budget < total_sum:
    print(f"The director needs {diff:.2f} leva more!")