needet_nylon_sq = int(input())
needet_paint_lt = int(input())
degreaser_lt = int(input())
needet_hours = int(input())

nylon_per_sq = 1.50
paint_per_lt = 14.50
degreaser_for_paint_per_lt = 5
bags = 0.4

price_nylon = (needet_nylon_sq + 2) * nylon_per_sq
price_for_paint = (needet_paint_lt * 1.1) * paint_per_lt
price_for_degreaser = degreaser_lt * degreaser_for_paint_per_lt

total_sum_materials = price_nylon + price_for_paint + price_for_degreaser + bags
sum_for_workers = (total_sum_materials * 0.30) * needet_hours
total_sum_for_repainting = total_sum_materials + sum_for_workers

print(total_sum_for_repainting)