# 미로 탐색
import sys, collections
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    q = collections.deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나거나 이동할 수 없으면 continue
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] += graph[x][y]

# 입력
n, m = map(int, input().split())

graph = [[0] * m] * n
for i in range(n):
    graph[i] = list(map(int, input().strip()))

bfs()

# 출력
print(graph[n-1][m-1])