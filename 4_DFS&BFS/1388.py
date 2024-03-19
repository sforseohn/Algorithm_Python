# 바닥 장식
# 장식을 바탕으로 나무 판자 개수 구하기
# dfs, 이어져 있으면 방문 체크 후 방문 X, 아니면 방문
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
directions = [(1, 0), (0, 1)]

def dfs(x, y):
    global ans
    
    visited[x][y] = 1
    nx, ny = x, y
    
    if floor[x][y] == '-': # 가로 무늬일 때 가로로만 탐색
        ny += 1
    else:
        nx += 1
    
    if nx < n and ny < m and floor[nx][ny] == floor[x][y] and not visited[nx][ny]:
        dfs(nx, ny)
        
        
# 입력   
n, m = map(int, input().split()) # 세로, 가로 크기
floor = [0] * n
for i in range(n):
    floor[i] = input().strip()

# 연산
ans = 0
visited = [[0] * m for _ in range(n)] # 방문 체크

for i in range(n):
        for j in range(m):
            if visited[i][j]:  # 이미 방문한 칸은 건너뛰기
                continue
            
            dfs(i, j)  
            ans += 1  # 한 번의 탐색이 완료되면 타일 하나 완성됨. 카운트 1 증가.
# 출력
print(ans)