food_kg = int(input())
count = 0
command = input()
while command != 'Adopted':
    food_grams = int(input())

    count_grams = food_kg * 1000
    count += food_grams
    if food_kg >=  food_grams:
        print(f"Food is enough! Leftovers: {count} grams.")

    else:
        print(f"Food is not enough. You need {count} grams more." )
    command = input()
