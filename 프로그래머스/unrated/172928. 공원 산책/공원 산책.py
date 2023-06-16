def solution(park, routes):
    answer = []
    direct = {'E':[0,1],'W':[0,-1],'N':[-1,0],'S':[1,0]}
    maxY = len(park[0])
    maxX = len(park)
    
    nowY,nowX = 0,0
    for i in range(len(park)):
        if 'S' in park[i]:
            nowX, nowY = i, park[i].find('S')
        park[i] = list(park[i])
    print(nowX,nowY)
    for route in routes:
        d,c = route.split()
        dx,dy = direct[d]
        nx,ny = nowX,nowY
        
        isPossible = True
        for _ in range(int(c)):
            ny,nx = ny+dy, nx+dx
            
            print(nx,ny)
            if nx < 0 or nx >= maxX or ny < 0 or ny >= maxY:
                print('bad1')
                isPossible = False
                break
            if park[nx][ny] == 'X':
                print('bad2')
                isPossible = False
                break
            if park[nx][ny] == 'O' or park[nx][ny] == 'S':
                print('cool')
                continue
                
        if isPossible:
            nowX, nowY = nx,ny
    return [nowX,nowY]