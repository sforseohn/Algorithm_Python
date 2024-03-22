import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

ans = 1e9
visited = []
w = []

def backtrack(n, cnt, cur, cost):
    global visited, ans, w
    if cost >= ans:
        return
    
    if cnt == n:
        if w[cur][0]:
            ans = min(ans, cost + w[cur][0])
        return
    
    for next in range(n):
        if w[cur][next] and not visited[next]:
            visited[next] = 1
            backtrack(n, cnt + 1, next, cost + w[cur][next])
            visited[next] = 0
            

def solution(n, cost):
    global visited, w
    
    w = cost
    visited = [0] * n
    visited[0] = 1
    backtrack(n, 1, 0, 0)    
    
    return ans
    

if __name__ == "__main__":
    # 입력
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    answer = solution(n, cost)
    print(answer)