time_line = '1h 45m,360s,25m,30m 120s,2h 60s'

time_line=time_line.replace(',', ' ')
time_line=time_line.split()

sum = 0

for i in time_line:
    if 'h' in i:
        number = int(i[:-1])
        sum += number*60
    elif 'm' in i:
        number = int(i[:-1])
        sum += number
    elif 's' in i:
        number = int(i[:-1])
        sum += number//60

print(sum)