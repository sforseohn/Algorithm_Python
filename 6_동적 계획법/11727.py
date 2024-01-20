# 2×n 타일링 2
import sys
input = sys.stdin.readline

# 입력
n = int(input()) # 2 * n 직사각형

# 연산
# 바로 앞이 정사각형이거나 세로 직사각형이거나
dp = [0, 1, 3] + [0] * (n-2) # dp 리스트 초기화

for i in range(3, n+1):
    dp[i] = dp[i-2] * (dp[2] - 1) + dp[i-1] * dp[1]
    dp[i] %= 10007

# 출력
print(dp[n])