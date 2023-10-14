loads_count = int(input())
venicle = ""
sum_loads = 0
for load in range(loads_count):
    tons_of_load = int(input())
    if tons_of_load <= 3:
        venicle == 'minibus'
    elif 4 >= tons_of_load < 11:
        venicle == 'Truck'
    elif tons_of_load > 12:
        venicle == 'Train'
