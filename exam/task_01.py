paper = int(input())
rolls = int(input())
glue = float(input())
discount = int(input())

price_paper = 5.80 * paper
rolls_price = 7.20 * rolls
price_glue = 1.20 * glue

total_sum = (price_paper + rolls_price + price_glue)
price_with_discount = total_sum - total_sum * discount / 100
print(f"{price_with_discount:.3f}")