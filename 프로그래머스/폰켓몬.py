from itertools import combinations


def solution(nums):
    answer = set()
    n = len(nums)//2

    monArr = set(nums)
    if len(monArr) >= n:
        answer = n
    elif len(monArr) < n:
        answer = len(monArr)

    return answer
