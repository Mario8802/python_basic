number = int(input())

min_number = int(input())
max_number = min_number
for i in range(number - 1):
    num = int(input())
    if num < min_number:
        min_number = num
    if num > max_number:
        max_number = num
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
