import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ps = input()
    stack = [ps[0]]
    result = "NO"
    for i in range(1, len(ps)):
        if len(stack) == 0:
            stack.append(ps[i])
        else:
            if ps[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ps[i])
            elif ps[i] == '(':
                stack.append(ps[i])

    if stack[0] == '\n':
        result = 'YES'
    print(result)
