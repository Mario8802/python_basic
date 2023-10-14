day_to_stay = int(input())
place_to_stay = input()
assessment = input()
price_per_night = 0
total_sum = 0
final_sum = 0

if place_to_stay == "room for one person":
    price_per_night = 18.00
    total_sum = price_per_night * day_to_stay - 18

elif place_to_stay == "apartment":
    if day_to_stay < 10:
        price_per_night = 25.00 * day_to_stay - 25
        total_sum = price_per_night * 0.70

    elif 10 <= day_to_stay <= 15:
        price_per_night = 25.00 * day_to_stay - 25
        total_sum = price_per_night * 0.65
    elif day_to_stay > 15:
        price_per_night = 25.00 * day_to_stay - 25
        total_sum = price_per_night * 0.50

elif place_to_stay == "president apartment":
    if day_to_stay < 10:
        price_per_night = 35.00 * day_to_stay - 35
        total_sum = price_per_night * 0.90

    elif 10 <= day_to_stay <= 15:
        price_per_night = 35.00 * day_to_stay - 35
        total_sum = price_per_night * 0.85
    elif day_to_stay > 15:
        price_per_night = 35.00 * day_to_stay - 35
        total_sum = price_per_night * 0.80

if assessment == 'positive':
    final_sum = total_sum + (total_sum * 0.25)

elif assessment == 'negative':
    final_sum = (total_sum * 0.90)

print(f"{final_sum:.2f}")
