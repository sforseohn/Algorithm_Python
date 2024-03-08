import sys
input = sys.stdin.readline

# 입력
n = int(input()) # 계단의 수
s = [0] * (n + 1)
for i in range(1, n+1):
    s[i] = int(input())
    
# 연산
dp = [0] * (n + 1)
dp[1] = s[1]
for i in range(2, n+1):
    # 현재로부터 한 칸 전이거나 두 칸 전
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

print(dp[-1])