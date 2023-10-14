flavor = input()
size = input()
price_set = int(input())

price = 0
discount = 0

if size == "small":

    if flavor == "Watermelon":
        price = 56 * 2
    if flavor == "Mango":
        price = 36.66 * 2
    if flavor == "Pineapple":
        price = 42.10 * 2
    if flavor == "Raspberry":
        price = 20 * 2

if size == "big":
    if flavor == "Watermelon":
        price = 28.70 * 5
    elif flavor == "Mango":
        price = 19.60 * 5
    elif flavor == "Pineapple":
        price = 24.80 * 5
    elif flavor == "Raspberry":
        price = 15.20 * 5
total_sum = price_set * price
total_sum_with_discount = total_sum - discount
if 400 <= total_sum and total_sum >= 1000:
    discount += total_sum * 0.15

# elif total_sum >= 1001:
#     discount = total_sum - (total_sum * 0.50)
#
total_sum_with_discount = total_sum - discount
print(discount)