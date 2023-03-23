def eratos(n):
    check = [True] * (n+1)
    check[0], check[1] = False, False
    
    for i in range(2,int(n**0.5)+1):
        for j in range(i+i, n+1, i):
            if check[j]:
                check[j] = False
    
    cnt = 0
    for v in check:
        if v == True:
            cnt+=1
    
    return cnt

def solution(n):
    answer = 0
    
    answer = eratos(n)
    return answer