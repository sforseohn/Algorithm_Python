# 평범한 배낭
import sys
input = sys.stdin.readline

# 입력
n, k = map(int, input().split())
knapsack = [(0, 0)]
for i in range(n):
    w, v = map(int, input().split())
    knapsack.append((w, v))

# 연산
dp = [[0] * (k+1) for _ in range(n+1)] # 무게가 최대 j인 배낭에 i번째 물건까지 담았을 때 가질 수 있는 최대 가치

for i in range(1, n+1):
    for j in range(1, k+1): # 무게만큼 반복
        w = knapsack[i][0]
        v = knapsack[i][1]
        
        if j < w: # 무게가 넘으면 이전 상태 유지
            dp[i][j] = dp[i-1][j] 
        else:     # 이전 상태 유지 vs 현재 넣을 무게만큼 빼고 현재 물건 넣기
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

# 출력
print(dp[n][k])

