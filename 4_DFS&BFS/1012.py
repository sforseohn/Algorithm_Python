# 유기농 배추
import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = collections.deque()
    visited[start_x][start_y] = 1
    queue.append((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:                
                visited[nx][ny] = 1     
                if graph[nx][ny]:                    
                    queue.append((nx, ny))           

# 입력
t = int(input())                      # 테스트 케이스의 수
    
# 연산
for _ in range(t):
    m, n, k = map(int, input().split())   # 가로, 세로, 배추 위치 수
    graph = [[0] * m for _ in range(n)]   # 배추밭
    visited = [[0] * m for _ in range(n)] # 방문 기록

    for _ in range(k):
        j, i = map(int, input().split())
        graph[i][j] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                visited[i][j] = 1
                if graph[i][j]:
                    bfs(i, j)
                cnt += 1
                
    # 출력
    print(cnt)