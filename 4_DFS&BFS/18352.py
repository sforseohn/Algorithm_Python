# 특정 거리의 도시 찾기
import sys, collections
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(x):
    ans = []
    queue = collections.deque()
    queue.append(x)
    visited[x] = 1 # 거리는 0이지만 방문 체크도 해주어야 하므로...
    
    while queue:
        u = queue.popleft()
        
        for n in graph[u]:
            if visited[n]:
                continue
            
            queue.append(n)

            visited[n] = visited[u] + 1
            if visited[n] == k+1:
                ans.append(n)         
    return ans
    
# 입력
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 방문 체크
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 단방향 연결

# 연산
ans = bfs(x)

# 출력
if not ans:
    print(-1)
else:
    for city in sorted(ans):
        print(city)