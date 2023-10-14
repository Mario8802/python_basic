

count_of_numbers = int(input())
total_sum = 0
first_number = int(input())
total_sum += first_number
max_num = first_number

for number in range(count_of_numbers - 1):
    current_num = int(input())
    total_sum += current_num
    if current_num > max_num:
        max_num = current_num
if max_num == total_sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - (total_sum - max_num))
    print("No")
    print(f"Diff = {diff}")

