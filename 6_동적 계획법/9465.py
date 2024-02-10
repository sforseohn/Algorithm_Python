# 스티커
import sys
input = sys.stdin.readline

# 입력
t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * 2
    
    for i in range(2):
        dp[i] = list(map(int, input().split()))

    # 연산
    # 대각선으로 이어졌거나 한 칸 건너뛴 경우
    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
    for j in range(2, n):
        for i in range(2):
            dp[i][j] += max(dp[not i][j - 1], dp[not i][j - 2])
        
    # 출력
    print(max(dp[0][-1], dp[1][-1]))