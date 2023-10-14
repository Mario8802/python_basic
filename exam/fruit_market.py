# calculation of fruits for a market

strawberries_price = float(input())
bananas_per_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

price_for_raspberries = strawberries_price / 2
orange_price = price_for_raspberries - (price_for_raspberries * 0.40)
price_for_bananas = price_for_raspberries * 0.20

sum_bananas = bananas_per_kg * price_for_bananas
sum_orange = orange_kg * orange_price
sum_raspberries = raspberries_kg * price_for_raspberries
sum_strawberries = strawberries_kg * strawberries_price

final_sum = sum_bananas + sum_orange + sum_raspberries + sum_strawberries
print(f"{final_sum:.2f}")