drink = input()
sugar = input()
count = int(input())
price = 0
discount_sugar = 0
discount_count = 0

if drink == "Espresso":
    if sugar == "Without":
        price = count * 0.90
        discount_sugar = price * 0.35
        price = price - discount_sugar

        if count > 5:
            discount_count = price * 0.25
            price = price - discount_count
            
    if sugar == "Normal":
        price = count * 1
    if sugar == "Extra":
        price = count * 1.20

if drink == "Cappuccino":
    if sugar == "Without":
        price = count * 1
    if sugar == "Normal":
        price = count * 1.20
    if sugar == "Extra":
        price = count * 1.60
    if price > 15:
        price = price - (price * 0.20)
if drink == "Tea":
    if sugar == "Without":
        price = count * 0.50
    if sugar == "Normal":
        price = count * 0.60
    if sugar == "Extra":
        price = count * 0.70
    if price > 15:
        price = price - (price * 0.20)


print(f"You bouht {count} cups of {drink} for {price:.2f} lv.")