# 바이러스 - BFS
import sys
import collections
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(r):
    cnt = 0 # 1번 컴퓨터는 제외
    visited[r] = 1
    q = collections.deque()
    q.append(r)
    
    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1
                cnt += 1
    
    return cnt

    
# 입력
n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결된 쌍의 수

# 간선 (1, n)
graph = [[] for _ in range(n+1)]

# 방문 체크
visited = [0] * (n+1)

# 양방향 연결
for _ in range(m): 
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연산 & 출력
print(bfs(1))