n1 = int(input())
n2 = int(input())
operator = input()

if operator == '+' or operator == '-' or operator == '*':
    result = 0
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'
    print(f"{n1} {operator} {n2} = {result} - {type_number}")
elif operator == '/' and n2 != 0 :
    print(f"{n1} / {n2} = {n1 / n2:.2f}")
elif operator == '%' and n2 != 0 :
    print(f"{n1} % {n2} = {n1 % n2}")
if n2 == 0:
    print(f"Cannot divide {n1} by zero")