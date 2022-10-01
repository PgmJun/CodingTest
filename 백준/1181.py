import sys
input = sys.stdin.readline

n = int(input().rstrip())  # n입력받기
word_list = list(set(input().rstrip() for _ in range(n)))
word_list.sort(key=len)
print(word_list)
max_cnt = len(word_list[-1])

result = []
for i in range(1, max_cnt+1):
    for j in word_list:
        if(len(j) == i):
            result.append(j)
    for w in sorted(result):
        print(w)
        result.clear()
