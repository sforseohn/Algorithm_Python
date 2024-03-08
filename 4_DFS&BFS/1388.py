# 바닥 장식
# 장식을 바탕으로 나무 판자 개수 구하기
# dfs, 이어져 있으면 방문 체크 후 방문 X, 아니면 방문
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
directions = [(1, 0), (0, 1)]

def dfs(x, y):
    global ans
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < m:
            if (floor[x][y] == floor[nx][ny] == '-' and x == nx) or (floor[x][y] == floor[nx][ny] == '|' and y == ny): # 하나의 조각
                if visited[nx][ny]:
                    ans -= 1
                else:
                    dfs(nx, ny)  
                    visited[nx][ny] = 1                     
            elif not visited[nx][ny]: # 다른 조각, 방문 X
                ans += 1 # 조각 추가
            
                dfs(nx, ny)  
                visited[nx][ny] = 1 
    
# 입력   
n, m = map(int, input().split()) # 세로, 가로 크기
floor = [0] * n
for i in range(n):
    floor[i] = input().strip()

# 연산
ans = 1
visited = [[0] * m for _ in range(n)] # 방문 체크
dfs(0, 0)

# 출력
print(ans)


'''
def dfs(x,y):
    # 바닥 장식 모양이 '-' 일 때
    if graph[x][y] == '-':
        graph[x][y] = 1	    # 해당 노드 방문처리
        for _y in [1,-1]:   # 양옆(좌우) 확인하기
            Y = y + _y
            # 좌우 노드가 주어진 범위를 벗어나지 않고 '-'모양이라면 재귀함수 호출
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x,Y)
    # 바닥 장식 모양이 '|' 일 때
    if graph[x][y] == '|':
        graph[x][y] = 1	    # 해당 노드 방문처리
        for _x in [1,-1]:   # 상하(위아래) 확인하기
            X = x + _x  
            # 상하 노드가 주어진 범위를 벗어나지 않고 '|' 모양이라면 재귀함수 호출
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X,y)
 
n,m = map(int, input().split()) # 방 바닥의 세로 크기 n, 가로 크기 m
graph = []  # 2차원 리스트의 맵 정보 저장할 공간
for _ in range(n):
    graph.append(list(input()))
 
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i,j)    # 노드가 '-'이나 '|'일 경우에 재귀함수 호출
            count += 1
'''