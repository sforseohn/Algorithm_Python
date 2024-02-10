# LCS
import sys
input = sys.stdin.readline

# 입력
a = input()
b = input()

# 연산
# 첫 번째 문자열의 i번째, 두 번째 문자열의 j번째까지 봤을 때
# 가장 긴 공통부분 문자열을 표현하는 2차원 배열
dp = [[0] * len(b) for _ in range(len(a))]
ans = 0

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i-1] == b[j-1]: # 두 수가 같으면 대각선 + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else:                # 두 수가 다르면 위옆 중 큰 수
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 출력
print(dp[-1][-1])