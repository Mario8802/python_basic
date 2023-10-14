count_detergent = int(input())
command = input()

#calculating dishwasher

leftover_detergent = 0
plate = 5
pot = 15
count_washes = 0
count_dishes = 0
count_pot = 0
while command != "End":
    leftover_detergent = (count_detergent * 750)

    count_washes += 1
    if count_washes == 3:
        count_pot += int(command)
        count_detergent -= count_pot * pot

    else:
        count_dishes += int(command)
        count_detergent -= count_dishes * plate
if leftover_detergent < 0:
    print(f"Not enough detergent, {abs(leftover_detergent)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{count_dishes} dishes and {count_pot} pots were washed.")
    print(f"Leftover detergent {leftover_detergent} ml.")

    command = int(input())