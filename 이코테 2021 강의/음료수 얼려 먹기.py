############################
# 알고리즘 공부할때 vscode가 개꿀이라 깔아놓고 단축키 세팅까지 해놨음
# Ctrl+S -> 저장하면 코드 줄 정리됨.
# 우측 상단에 화살표 빌드 모양 누르고 터미널에 입력값을 마우스 우클릭으로 입력하고 엔터하면 됨.
# 빌드 단축키도 설정할 수 있는데 그건 찾아보센
# 그리고 밑에 코드 사이에 피드백 써놨음
############################


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        # 해당노드 방문처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


# n,m을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())


##########################
# '00000' 이랑 '0 0 0 0 0' 은 다름
# split() 함수는 기본 값이 ' ' << 한 칸 공백이므로 공백없이 붙어있는 '00000'은 split이 안 됨.
# 만약 '00000'을 list로 만들고 싶으면 그냥 list('00000') => ['0', '0', '0', '0', '0'] 이 됨.
# 배열의 요소를 int로 만들고 싶으면 list(map(int, ['0','0','0','0','0'])) => [0, 0, 0, 0, 0]
##########################

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    # 이전 코드 : graph.append(list(map(int,input().split())))
    graph.append(list(map(int, input())))


# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
