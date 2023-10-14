# calculating the size of aquarium

leight = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium_volume = leight * width * height
volume_in_liters = aquarium_volume * 0.001

occupied_space = volume_in_liters * 0.83
print(occupied_space)