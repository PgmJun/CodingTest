stack = []
n = int(input())

for i in range(n):
    v = input()
    if v == '0':
        stack.pop()
        continue
    stack.append(int(v))

print(sum(stack))
