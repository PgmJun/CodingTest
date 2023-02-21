import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list()

for _ in range(int(input())):
    command = list(input().split())

    if command[0] == 'P':
        s1.append(command[1])

    elif command[0] == 'L':  # 커서를 왼쪽으로 한 칸 옮김
        if len(s1) > 0:
            s2.append(s1.pop())

    elif command[0] == 'D':  # 커서를 오른쪽으로 한 칸 옮김
        if len(s2) > 0:
            s1.append(s2.pop())

    elif command[0] == 'B':  # 커서 왼쪽에 있는 문자를 삭제함
        if len(s1) > 0:
            s1.pop()

s1.extend(reversed(s2))
print(''.join(s1))
