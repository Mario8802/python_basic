movie = input()
package_movie = input()
tickets_count = int(input())
discount = 0

if movie == "John Wick":
    if package_movie == "Drink":
        price = 12 * tickets_count
    elif package_movie == "Popcorn":
        price = 15 * tickets_count
    elif package_movie == "Menu":
        price = 19 * tickets_count
if movie == "Star Wars":
    if package_movie == "Drink":
        price = 18 * tickets_count
    elif package_movie == "Popcorn":
        price = 25 * tickets_count
    elif package_movie == "Menu":
        price = 30 * tickets_count
    if tickets_count >= 4:
        discount = price * 0.30
if movie == "Jumanji":
    if package_movie == "Drink":
        price = 9 * tickets_count
    elif package_movie == "Popcorn":
        price = 11 * tickets_count
    elif package_movie == "Menu":
        price = 14 * tickets_count
    if tickets_count == 2:
        discount = price * 0.15

total_sum = price - discount


print(f"Your bill is {total_sum:.2f} leva.")