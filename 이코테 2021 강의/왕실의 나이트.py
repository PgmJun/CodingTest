loc = input() #값 입력
locX = ['a','b','c','d','e','f','g','h'] #x좌표 인덱스
locY = ['1','2','3','4','5','6','7','8'] #y좌표 인덱
cnt = 0 # 이동 가능한 경우의 수

#상단 오른쪽부터 시계방향으로 이동 범위
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]

x = locX.index(loc[0])+1 #x좌표값 구하기
y = locY.index(loc[1])+1 #y좌표값 구하기

#이동한 x,y의 위치가 1이상이면 카운트
for i in range(len(dx)):
    if x+dx[i] > 0 and y+dy[i]>0:
        cnt+=1

print(cnt)
        
