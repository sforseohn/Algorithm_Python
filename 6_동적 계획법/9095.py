# 1, 2, 3 더하기
import sys
input = sys.stdin.readline

MAX_N = 11

# 연산
# 11까지 한 번에 구하기
a = [0, 1, 2, 4] + [0] * (MAX_N - 3)

for i in range(4, MAX_N):
    a[i] = a[i-1] + a[i-2] + a[i-3]

# 입력 & 출력
t = int(input()) # 테스트 케이스의 수

for i in range(t):
    n = int(input())
    print(a[n])