global cnt


def find(idx, val):
    global cnt
    if idx >= n:
        return

    val += arr[idx]
    if val == s:
        cnt += 1

    find(idx+1, val)
    find(idx+1, val - arr[idx])


n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

find(0, 0)
print(cnt)
