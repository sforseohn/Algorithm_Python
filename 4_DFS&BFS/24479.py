# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = cnt # 방문 체크
    graph[v].sort()
    for w in graph[v]:
        if visited[w]:
            continue
        dfs(w)

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
cnt = 0
dfs(r)

# 출력
for v in visited[1:]:
    print(v)