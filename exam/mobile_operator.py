duration_of_contract = input()
type_of_a_contract = input()
added_mobile_internet = input()
number_of_months_to_pay = int(input())
price = 0
discount = 0
mobile_internet_price = 0
if duration_of_contract == "one":
    if type_of_a_contract == "Small":
        price = 9.98
    elif type_of_a_contract == "Middle":
        price = 18.99
    elif type_of_a_contract == "Large":
        price = 25.98
    elif type_of_a_contract == "ExtraLarge":
        price = 35.99


if duration_of_contract == "two":
    discount = 0.0375
    if type_of_a_contract == "Small":
        price = 8.58
    elif type_of_a_contract == "Middle":
        price = 17.09
    elif type_of_a_contract == "Large":
        price = 23.59
    elif type_of_a_contract == "ExtraLarge":
        price = 31.79


if added_mobile_internet == "yes" and price <= 10:
    mobile_internet_price += 5.50
elif added_mobile_internet == "yes" and price <= 30:
    mobile_internet_price += 4.35
elif added_mobile_internet == "yes" and price > 30:
    mobile_internet_price += 3.85
if duration_of_contract == "two":
    total_sum = (price + mobile_internet_price) * number_of_months_to_pay
    final_sum_with_discount = total_sum - (total_sum * 0.0375)
total_sum = (price + mobile_internet_price) * number_of_months_to_pay
final_sum_with_discount = total_sum - (total_sum * discount)
# print(total_sum)
print(f"{final_sum_with_discount:.2f} lv.")