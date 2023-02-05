ans = []

while True:
    l, p, v = map(int, input().split())
    if (l + p + v) == 0:
        break
    date = (v // p) * l
    remainDate = v % p
    if remainDate >= l:
        date += l
    else:
        date += remainDate
    ans.append(date)

for i in range(len(ans)):
    print('Case {}: {}'.format(i+1, ans[i]))
