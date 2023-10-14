record_in_sec = float(input())
distance_in_meters = float(input())
time_in_sec_per_meter = float(input())
from math import floor

total_sec = distance_in_meters * time_in_sec_per_meter
delay = floor(distance_in_meters / 50) * 30
total_time_with_delay = (total_sec + delay)
diff = abs(total_time_with_delay - record_in_sec)

if record_in_sec <= total_time_with_delay:
    print(f"No! He was {diff:.2f} seconds slower.")
elif record_in_sec >= total_time_with_delay:
    print(f"Yes! The new record is {total_time_with_delay:.2f} seconds.")
