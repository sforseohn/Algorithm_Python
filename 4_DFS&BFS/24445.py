# 알고리즘 수업 - 너비 우선 탐색 1
import sys
import collections
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(r):
    cnt = 1
    visited[r] = cnt # 방문 체크
    q = collections.deque()
    q.append(r)
    graph[r].sort() 
    
    while q:
        u = q.popleft()
        graph[u].sort(reverse=True) # 인접 정점은 오름차순으로 방문
        for w in graph[u]:
            if not visited[w]:
                cnt += 1
                visited[w] = cnt
                q.append(w)

# 입력
n, m, r = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점

# 간선 (1, n)
graph = [[] for _ in range(n+1)]

# 방문 체크
visited = [0] * (n+1)

# 양방향 연결
for _ in range(m): 
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연산
bfs(r)

# 출력
for v in visited[1:]:
    print(v)