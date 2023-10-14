model_computer = int(input())

count_sales = 0
rating_count = 0

for i in range(model_computer):

    sales_rating = int(input())

    rating = sales_rating % 10
    possible_sales = sales_rating // 10

    if rating == 2:
        sales = 0
        count_sales += sales
        rating_count += rating

    elif rating == 3:
        sales = 0.5 * possible_sales
        count_sales += sales
        rating_count += rating

    elif rating == 4:
        sales = 0.7 * possible_sales
        count_sales += sales
        rating_count += rating

    elif rating == 5:
        sales = 0.85 * possible_sales
        count_sales += sales
        rating_count += rating

    elif rating == 6:
        sales = possible_sales
        count_sales += sales
        rating_count += rating

    i += 1

average_rating = rating_count / model_computer

print(f"{count_sales:.2f}")
print(f"{average_rating:.2f}")