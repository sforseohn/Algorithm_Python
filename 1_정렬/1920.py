import sys
input = sys.stdin.readline

# 입력
n = int(input())
a = set(map(int, input().split())) # set 사용
m = int(input())
nums = list(map(int, input().split()))

# 연산 & 출력
for i in range(m):
    if nums[i] in a:
        print(1)
    else:
        print(0)