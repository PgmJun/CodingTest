for i in range(1):
    n = int(input())
    sum = 0
    for j in range(n):
        sum += int(input())
    if sum == 0:
        print(0)
    elif sum > 0:
        print('+')
    else:
        print('-')