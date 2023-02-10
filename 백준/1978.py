import math


def is_prime_number(nlist):
    cnt = 0
    for x in nlist:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                break
        cnt += 1
    return cnt


n = input()
nlist = list(map(int, input().split()))
print(is_prime_number(nlist))
