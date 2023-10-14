packege_of_pens = int(input())
packege_of_markers = int(input())
detergent_liters = int(input())
percent_discount = int(input())

price_for_pens = packege_of_pens * 5.80
price_for_markers = packege_of_markers * 7.20
price_for_detergent = detergent_liters * 1.20

total_sum = price_for_pens + price_for_markers + price_for_detergent
total_sum_with_discount = total_sum - total_sum * (percent_discount / 100)
print(total_sum_with_discount)