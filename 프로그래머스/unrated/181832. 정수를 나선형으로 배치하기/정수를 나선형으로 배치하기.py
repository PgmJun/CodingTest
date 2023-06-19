def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    dir = 'r'
    x,y = 0,0
    
    for i in range(1, (n**2)+1):
        answer[x][y] = i
        
        if dir == 'r':
            if y < n-1 and answer[x][y+1] == 0:
                y += 1
                continue
            dir = 'd'
            x += 1
            
        elif dir == 'd':
            if x < n-1 and answer[x+1][y] == 0:
                x += 1
                continue
            dir = 'l'
            y -= 1
            
        elif dir == 'l':
            if y > 0 and answer[x][y-1] == 0:
                y -= 1
                continue
            dir = 't'
            x -= 1
        
        elif dir == 't':
            if x > 0 and answer[x-1][y] == 0:
                x -= 1
                continue
            dir = 'r'
            y += 1
        
            
            
    return answer