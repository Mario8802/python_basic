total_pages_to_read = int(input())
pages_per_hour = int(input())
days = int(input())

total_time_for_reading = total_pages_to_read // pages_per_hour
needet_hours_per_day = total_time_for_reading // days

print(needet_hours_per_day)