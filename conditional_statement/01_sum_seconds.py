first_time = int(input())
sec_time = int(input())
third_time = int(input())
tot_time = first_time + sec_time + third_time
minutes = tot_time // 60
seconds = tot_time % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

first_time = int(input())
sec_time_time = int(input())
third_time = int(input())

total_time = first_time + sec_time + third_time
minutes = total_time // 60
seconds = total_time % 60
if seconds < 10:
    print(f"{minutes}:0")