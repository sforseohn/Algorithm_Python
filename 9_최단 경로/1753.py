import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# 입력
v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1) # 최단거리 테이블

for _ in range(e):
    u, V, w = map(int, input().split())
    graph[u].append((V, w)) # 가중치, 목적 노드

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q) # 최소 거리와 정점 꺼내기
        
        if distance[node] < dist:
            continue
        
        for to, cost in graph[node]:
            new_dist = dist + cost
            if new_dist < distance[to]:
                distance[to] = new_dist
                heapq.heappush(q, (distance[to], to))
        
dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])