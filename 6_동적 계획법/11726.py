# 2 * n 타일링
import sys
input = sys.stdin.readline

def solution(n):
    if n == 1: # 예외 처리
        return 1
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] += dp[i-1] + dp[i-2]
    
    return dp[n]
    
n = int(input())

print(solution(n) % 10007)