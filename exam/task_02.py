cash_per_day = float(input())
income_per_day = float(input())
outcome_per_day = float(input())
present = float(input())
days = 5

saved_money = days * cash_per_day
income = days * income_per_day
total_income = saved_money + income
total_income_without_expenses = total_income - outcome_per_day

if total_income_without_expenses >= present:
    print(f"Profit: {total_income_without_expenses:.2f} BGN, the gift has been purchased.")
if total_income_without_expenses < present:
    diff = abs(total_income_without_expenses - present)
    print(f"Insufficient money: {diff:.2f} BGN.")



