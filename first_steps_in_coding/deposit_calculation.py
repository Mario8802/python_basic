deposit = int(input())
months = int(input())
annual_rate = float(input())

annual_rate_per_year = deposit * annual_rate / 100
annual_rate_per_month = annual_rate_per_year / 12
total_sum = deposit + months * annual_rate_per_month

print(total_sum)