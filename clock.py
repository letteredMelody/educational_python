time_before = int(input())
time_after = time_before + int(input())

hours = (time_before // 3600) % 24
time_before %= 3600
minutes = (time_before // 60) % 60
seconds = time_before % 60

print(hours, minutes, seconds)

hours = (time_after // 3600) % 24
time_after %= 3600
minutes = (time_after // 60) % 60
seconds = time_after % 60

print(hours, minutes, seconds)