import itertools

# 에라토스테네스의 체 알고리즘
# n+1개의 소수 체크 리스트 생성(모두 소수(True)인 것으로 초기화)
# 0,1은 소수가 아니므로 False로 변경

# 2부터 n의 제곱근 까지만 확인
# 2부터 n의 배수들을 소수가 아닌 것(False)으로 처리

# numbers로 만들 수 있는 수가 소수이면 answer+=1 (check[num] == True: answer+=1)
def findSosu(n):
    check = [True] * (n+1)
    sosuArr = []
    check[0],check[1] = False,False
    for i in range(2, int(n**0.5) + 1):
        for j in range(i+i,n+1,i):
            if check[j] == True:
                check[j] = False

    return check

def solution(numbers):
    answer = 0
    numArr = set()
    for i in range(1,len(numbers)+1):
        for n in itertools.permutations(numbers,i):
            v = int(''.join(n))
            if v in numArr:
                continue
            numArr.add(v)
    
    check = findSosu(max(numArr))
    
    for num in numArr:
        if check[num]:
            answer += 1
    
    return answer