import sys
from itertools import permutations
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

MAX_N = 8

# 입력
n, m = map(int, input().split())
nums = list(map(int, input().split()))
sequence = [0] * m

# 연산
perms = sorted(list(permutations(nums, m)))
for perm in perms:
    print(*perm)
    