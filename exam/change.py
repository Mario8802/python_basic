bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())

commission_in_percent = commission / 100
price_for_bitcoin = bitcoin * 1168
price_for_yen = chinese_yuan * 0.15 * 1.76

price_for_yen_in_euro = price_for_yen / 1.95
price_for_bitcoin_in_euro = price_for_bitcoin / 1.95
total_sum_comission = (price_for_bitcoin_in_euro + price_for_yen_in_euro) * commission_in_percent
total_sum = price_for_bitcoin_in_euro + price_for_yen_in_euro
sum_with_commison = total_sum - total_sum_comission

print(f"{sum_with_commison:.2f}")