city = input()
package = input()
vip = input()
days = int(input())
price = 0
discount = 0

if city == "Bansko" or "Borovets":
    if package == "noEquipment":
        price = days * 100
        if vip == "Yes":
            discount == price * 444
    if package == "withEquipment":
        price = 80
        if vip == "Yes":
            price == price - (price * 0.05)
if city == "Varna" or "Burgas":
    if package == "noBreakfast":
        price = 130
        if vip == "Yes":
            price == price - (price * 0.12)
    if package == "withBreakfast":
        price = 100
        if vip == "Yes":
            price == price - (price * 0.07)

#
# if days > 7:
#     days = days - 1
# if days < 1:
#     print("Days must be a positive number")
# else:
#     print("Invalid input")
# print(f"The price is {price:.2f}lv! Have a nice time!")
print(discount)
