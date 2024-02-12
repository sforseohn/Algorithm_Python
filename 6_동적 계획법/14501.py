# 퇴사
import sys
input = sys.stdin.readline

# 입력
n = int(input())
time = []
pay = []
for i in range(n):
    t, p = map(int, input().split()) # 상담을 완료하는 데 걸리는 시간, 금액
    time.append(t)
    pay.append(p)

# 연산
dp = [0] * (n+1)
max_pay = 0
for i in range(n):
    max_pay = max(max_pay, dp[i])
    if i + time[i] > n:
        continue
    dp[i + time[i]] = max(max_pay + pay[i], dp[i+time[i]])
            
# 출력
print(max(dp))
