# 가장 긴 바이토닉 부분 수열
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 입력
n = int(input())
a = list(map(int, input().split()))

# 연산
# dp[i] : i번째 수를 마지막 원소로 가지는 부분 수열의 최대 길이
# [증가수열, 감소수열]일 때 최댓값
dp = [[1, 1] for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        # 증가수열 업데이트
        if a[j] < a[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        
        # 감소수열 업데이트
        if a[j] > a[i]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1, dp[j][0] + 1)
            
# 출력
max_a = max(dp, key=lambda x: max(x))
print(max(max_a))