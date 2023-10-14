numbers_of_packet_of_pens = int(input())
numbers_of_packets_of_markers = int(input())
liters_of_chalkboard_cleaner = int(input())
percent_discount = int(input())
price_per_pen = 5.80
price_per_marker = 7.20
price_for_chalkboard_cleaner = 1.20
total_sum = numbers_of_packet_of_pens * price_per_pen \
            + numbers_of_packets_of_markers * price_per_marker \
            + liters_of_chalkboard_cleaner * price_for_chalkboard_cleaner
total_sum = total_sum - total_sum * (percent_discount / 100)
print (total_sum)