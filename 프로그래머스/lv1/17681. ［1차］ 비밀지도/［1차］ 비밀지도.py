EMPTY = ' '
WALL = '#'
def solution(n, arr1, arr2):
    wall1, wall2 = list(), list()
    
    
    for a in arr1:
        wall = str(format(a, 'b').zfill(n))
        wall1.append(wall)
        
    for a in arr2:
        wall = str(format(a, 'b').zfill(n))
        wall2.append(wall)
    
        
    graph = ['' for _ in range(n)]

    print(wall1, wall2)
    for i in range(n):
        for j in range(n):
            if wall1[i][j] == '1' or wall2[i][j] == '1':
                print(i,j)
                graph[i]+='#'
                continue
            graph[i]+=' '
    print(graph)
    return graph