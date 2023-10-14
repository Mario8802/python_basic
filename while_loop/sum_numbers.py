CONSTANT_NUMBER = int(input())
sum_all_numbers = 0

while True:
    current_number = int(input())
    sum_all_numbers += current_number

    if sum_all_numbers >= CONSTANT_NUMBER:
        print(sum_all_numbers)
        break