import sys
input = sys.stdin.readline

n = int(input().rstrip())
dlist = []
for _ in range(n):
    dlist.append(list(map(int, input().rstrip().split())))

for d in dlist:
    rank = 1
    for i in dlist:  # 자기보다 덩치 큰 사람이 있으면 rank 다운하는 로직
        if d[0] < i[0] and d[1] < i[1]:
            rank += 1
    print(rank, end=' ')
