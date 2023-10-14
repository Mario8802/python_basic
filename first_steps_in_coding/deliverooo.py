chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

price_for_chicken_menu = chicken_menu * 10.35
price_for_fish_menu = fish_menu * 12.40
price_for_veggie_menu = veggie_menu * 8.15

total_menus = price_for_veggie_menu + price_for_fish_menu + price_for_chicken_menu
price_for_desert = total_menus * 0.20
total_sum = total_menus + price_for_desert + 2.50

print(total_sum)