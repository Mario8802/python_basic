needed_money = float(input())
init_money = float(input())
total_sum = init_money
count_spend_days = 0
count_total_days = 0
while total_sum < needed_money:
    if count_spend_days == 5:
        break
    action = input() # spend / save
    amount = float(input())
    count_total_days = 0

    if action == "spent":
        total_sum -= amount
        count_spend_days += 1
        if total_sum < 0:
            total_sum = 0
    else:
        count_spend_days = 0
        total_sum += amount
if count_spend_days == 5:
    print("You can't save the money.")
    print(count_total_days)
else:
    print(f"You saved the money for {count_total_days} days.")