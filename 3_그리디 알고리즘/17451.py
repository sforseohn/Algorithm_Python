# 평행 우주
import sys
input = sys.stdin.readline

# 입력
n = int(input())
v = list(map(int, input().split()))

# 연산
ans = 0
for i in range(n-1, -1, -1):
    if ans > v[i] and not ans % v[i]: # 모든 조건 만족
        continue
    else:                             # v보다 큰 배수로 만들어주어야 함
        ans = v[i] * (ans // v[i] + 1)

# 출력
print(ans)

'''
for i in range(n-1, -1, -1):
    if ans < v[i]:   # 속도 더 필요
        ans = v[i]
    elif ans % v[i]: # 배수로 만들어주어야 함
        ans = v[i] * (ans // v[i] + 1)
    else:            # 모든 조건 만족
        continue

'''