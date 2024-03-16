# 외판원 순회 2
import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력
n = int(input())
w = [0] * n
for i in range(n):
    w[i] = list(map(int, input().split()))

# 연산
visited = [0] * n
min_cost = INF

def backtrack(cnt, node, cost):
    global min_cost
    if cost >= min_cost:
        return
    
    if cnt == n-1: # n-1개의 도시 탐색
        if not w[node][0]:
            return
        
        cost += w[node][0]
        min_cost = min(min_cost, cost)
    
    visited[node] = 1
    
    for i in range(n):
        if not w[node][i] or visited[i]:
            continue
        
        visited[i] = 1
        
        backtrack(cnt + 1, i, cost + w[node][i])
        
        visited[i] = 0
        
backtrack(0, 0, 0)

print(min_cost)

