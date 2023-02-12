cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

x, y = map(int, input().split())

now = y
for i in range(x):
    now += cal[i]

print(day[now % 7])
