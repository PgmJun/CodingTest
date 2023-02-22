n = int(input())
p = list(map(int, input().split()))

answer = 0
before = 0
for time in sorted(p):
    before += time
    answer += before

print(answer)
