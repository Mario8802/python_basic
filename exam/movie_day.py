time_for_filming = int(input())
number_of_scenes = int(input())
time_for_scene = int(input())
from math import floor, ceil
preparing_terrain = time_for_filming * 0.15
time_for_filming_the_scenes = number_of_scenes * time_for_scene

total_time_for_filming_the_movie = preparing_terrain + time_for_filming_the_scenes
diff = abs(time_for_filming - total_time_for_filming_the_movie)

if total_time_for_filming_the_movie > time_for_filming:
    print(f"Time is up! To complete the movie you need {ceil(diff)} minutes.")

else:
    print(f"You managed to finish the movie on time! You have {ceil(diff)} minutes left!")