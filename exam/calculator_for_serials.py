name = input()
num_seasons = int(input())
num_episodes = int(input())
time_without_ads = float(input())
# calculating the time for wathing seriеs
ad = time_without_ads * 0.20
full_episode = time_without_ads + ad
last_episode = num_seasons * 10

time = (full_episode * num_episodes * num_seasons) + last_episode

print(f"Total time needed to watch the {name} series is {int(time)} minutes.")

