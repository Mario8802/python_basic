destination = input()
saved_money = 0

while destination != "End":
    needed_money = float(input())

    while saved_money <= needed_money:
        budget = float(input())
        saved_money += budget

        if saved_money >= needed_money:
            print(f"Going to {destination}!")
            break

    saved_money = 0
    destination = input()