# 정수 삼각형
import sys
input = sys.stdin.readline

# 입력
n = int(input())   # 삼각형의 크기

dp = [0] * n # 삼각형 수 저장
for i in range(n):
    dp[i] = list(map(int, input().split()))

# 연산
for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])

# 출력
print(dp[0][0])