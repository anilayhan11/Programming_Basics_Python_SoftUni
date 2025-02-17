import math

series_name = input()
duration_episode = int(input())
duration_break = int(input())

lunch_time = duration_break / 8
rest_time = duration_break / 4
time_for_series = duration_break - (lunch_time + rest_time)
time_left = time_for_series - duration_episode
time_needed = duration_episode - time_for_series

if duration_episode <= time_for_series:
    print(f'You have enough time to watch {series_name} and left with {math.ceil(time_left)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {series_name}, you need {math.ceil(time_needed)} more minutes.')

