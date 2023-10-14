baggage_over_20 = float(input())
baggage_kg = float(input())
days_to_the_trip = int(input())
count_baggage = int(input())


baggage_price = 0

if baggage_kg < 10:
    baggage_price = baggage_over_20 * 0.20

elif 10 < baggage_kg <= 20:
    baggage_price = baggage_over_20 / 2
else:
    baggage_price = baggage_over_20
if days_to_the_trip > 30:
    baggage_price = baggage_price * 0.10 + baggage_price
elif 7 < days_to_the_trip <= 30:
    baggage_price = baggage_price * 0.15 + baggage_price
elif days_to_the_trip < 7:
    baggage_price = baggage_price * 0.40 + baggage_price
total_sum = baggage_price * count_baggage

print(f"The total price of bags is: {total_sum:.2f} lv.")