movie = input()
count_days = int(input())
count_tickets = int(input())
price_tickets = float(input())
percent_for_cinema = int(input())

price_for_tickets_per_day = count_tickets * price_tickets
income_for_whole_time = count_days * price_for_tickets_per_day
income_percent_for_the_cinema = income_for_whole_time * percent_for_cinema / 100
total_income = income_for_whole_time - income_percent_for_the_cinema

print(f"The profit from the movie {movie} is {total_income:.2f} lv.")