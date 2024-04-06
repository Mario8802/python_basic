visitors = int(input())

back = 0
chest = 0
legs = 0
abs_count = 0
protein_shake = 0
protein_bar = 0
for _ in range(1,visitors + 1):
    command = input()
    if command == "Back":
        back += 1
    elif command == "Chest":
        chest += 1
    elif command == "Legs":
        legs += 1
    elif command == "Abs":
        abs_count += 1
    elif command == "Protein shake":
        protein_shake += 1
    elif command == "Protein bar":
        protein_bar += 1

total_work_out = back + chest + legs + abs_count
total_protein = protein_shake + protein_bar

work_out_percentage = (total_work_out / visitors) * 100
protein_percentage = (total_protein / visitors) * 100


print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out_percentage:.2f}% - work out")
print(f"{protein_percentage:.2f}% - protein")
