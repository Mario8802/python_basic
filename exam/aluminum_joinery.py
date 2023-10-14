aluminum_joinery_count = int(input())
type_of_aluminum_joinery = input()
delivery = input()
price = 0

delivery_tax = 0
from sys import exit
if aluminum_joinery_count <= 10:
    print("Invalid order")
    exit()

if type_of_aluminum_joinery == "90X130":
    if 30 < aluminum_joinery_count <= 60:
        price = (aluminum_joinery_count * 110) * 0.95
    elif aluminum_joinery_count > 60:
        price = (aluminum_joinery_count * 110) * 0.92

if type_of_aluminum_joinery == "100X150":
    if 40 <= aluminum_joinery_count <= 80:
        price = (aluminum_joinery_count * 140) * 0.94
    elif aluminum_joinery_count > 80:
        price = (aluminum_joinery_count * 140) * 0.90

if type_of_aluminum_joinery == "130X180":
    if 20 < aluminum_joinery_count <= 50:
        price = (aluminum_joinery_count * 190) * 0.93
    elif aluminum_joinery_count >= 50:
        price = (aluminum_joinery_count * 190) * 0.88

if type_of_aluminum_joinery == "200X300":
    if 20 < aluminum_joinery_count <= 50:
        price = (aluminum_joinery_count * 250) * 0.91
    elif aluminum_joinery_count >= 50:
        price = (aluminum_joinery_count * 250) * 0.86

if delivery == "With delivery":
    total_sum = price + delivery_tax + 60
else:

    var = delivery == "Without delivery"
    total_sum = price

if aluminum_joinery_count > 99:

    total_sum = (total_sum - (total_sum * 0.04))
else:
    total_sum = total_sum
print(f"{total_sum:.2f} BGN")
