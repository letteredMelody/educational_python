def seconds_to_time(sec):
    hours = (sec // 3600) % 24
    sec %= 3600
    minutes = (sec // 60) % 60
    sec = sec % 60
    
    return f'{hours}h {minutes}m {sec}s'

time_before = int(input())
time_after = time_before + int(input())

print('Before: '+ seconds_to_time(time_before))
print('After: '+ seconds_to_time(time_after))