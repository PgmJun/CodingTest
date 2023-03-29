def solution(n, k):
    answer = 0
    serviceDrink = n//10
    
    k -= serviceDrink
    
    answer += (n * 12000)
    answer += (k * 2000)
    return answer