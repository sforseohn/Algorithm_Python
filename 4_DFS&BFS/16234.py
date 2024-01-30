# 인구 이동
import sys, collections
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(start_x, start_y):
    global flag, graph
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = collections.deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1
    node_list = []
    group_sum = 0
    
    while queue:
        x, y = queue.popleft()
        group_sum += graph[x][y]
        node_list.append((x, y))
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1  # 방문 체크를 여기서 해야 함
    # 인구 수 갱신         
    if len(node_list) > 1: 
        flag = False
        population = group_sum // len(node_list)
        for x, y in node_list:
            graph[x][y] = population
                    

# 입력
n, l, r = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

# 연산
day = 0
while True:
    flag = True
    visited = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                bfs(i, j)
    
    if flag: # 인구 이동이 없으면
        break
    day += 1 # 날짜 갱신

# 출력
print(day)

'''
to_seek = collections.deque() # 탐색해야 할 정점
    to_seek.append((0, 0)) 
    while to_seek:
        x, y = to_seek.popleft()
        if not visited[x][y]:
            bfs(x, y)
'''