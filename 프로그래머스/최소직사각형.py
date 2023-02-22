def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort(reverse=True)
        
    maxW, maxH = 0,0
    for w,h in sizes:
        maxW = max(maxW,w)
        maxH = max(maxH,h)
    
    answer = maxW * maxH
    return answer