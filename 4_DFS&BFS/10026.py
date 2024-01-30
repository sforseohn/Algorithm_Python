# 적록색약
import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    zone = 0     # 구역 수
    
    queue = collections.deque()
    visited[start_x][start_y] = 1
    queue.append((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:                
                if board[nx][ny] == board[x][y]:                    
                    queue.append((nx, ny))
                    visited[nx][ny] = 1                
    return zone

# 입력
n = int(input())              # 그림의 크기
board = [[] for _ in range(n)]        # 그림 정보
visited = [[0] * n for _ in range(n)] # 방문 기록

for i in range(n):
    board[i] = list(input().strip())
    
# 연산
not_ans, cb_ans = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j)
            not_ans += 1

visited = [[0] * n for _ in range(n)]
for i in range(n):
      for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j)
            cb_ans += 1

# 출력
print(not_ans, cb_ans)