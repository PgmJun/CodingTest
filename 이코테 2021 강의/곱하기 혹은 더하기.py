#0~9로만 이루어진 문자열S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩
#모든 숫자를 확인하며 숫자 사이에 * 혹은 + 연산자를 넣어
#결과적으로 만들어 질 수 있는 가장 큰 수를 구하는 프로그램을 작성
#연산은 왼쪽부터 오른쪽으로 순서대로 이루어짐

import sys
input=sys.stdin.readline

n = input()
result = int(n[0])

for i in range(1,len(n)-1):
    num = int(n[i])
    
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)
