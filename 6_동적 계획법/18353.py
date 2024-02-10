# 병사 배치하기
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 입력
n = int(input())
power = list(map(int, input().split()))

# 연산
power.reverse() # 전투력이 작은 순으로 정렬
dp = [1] * n    # dp[i] : i번째 수를 마지막 원소로 가지는 부분 수열의 최대 길이

## 최장 증가 부분 수열 문제 (LIS)
# 각 요소를 순회하며
# 앞 요소 중 자신보다 작은 수가 있다면 dp 업데이트
for i in range(1, n):
    for j in range(0, i):
        if power[j] < power[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
# 출력
print(n - max(dp))  # 총 인원 - 최장 수열