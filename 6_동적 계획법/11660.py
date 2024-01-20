# 구간 합 구하기 5
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split()) # 표의 크기, 합을 구하는 횟수

dp = [[0] for _ in range(n+1)] # (1, 1)부터 시작
dp[0] = [0] * (n+1)
for i in range(n):
    dp[i+1] += map(int, input().split())

# 연산 & 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] # 앞 행, 열까지의 합 저장
        
for _ in range(m):
    x1, y1, x2, y2  = map(int, input().split())
    
    ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    
    print(ans)
