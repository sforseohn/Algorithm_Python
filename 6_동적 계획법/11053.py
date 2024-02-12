# 가장 긴 증가하는 부분 수열
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 입력
n = int(input())
a = list(map(int, input().split()))

# 연산
dp = [1] * n    # dp[i] : i번째 수를 마지막 원소로 가지는 부분 수열의 최대 길이

## 최장 증가 부분 수열 문제 (LIS)
# 각 요소를 순회하며
# 앞 요소 중 자신보다 작은 수가 있다면 dp 업데이트
for i in range(1, n):
    for j in range(0, i):
        if a[j] < a[i]: # i가 j보다 클 때 j에 있는 최대길이 가져옴
            dp[i] = max(dp[i], dp[j] + 1)
            
# 출력
print(max(dp)) 