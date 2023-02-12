n = int(input())
numbers = input()

sum = 0
for num in numbers:
    if num == '0':
        continue
    sum += int(num)

print(sum)
