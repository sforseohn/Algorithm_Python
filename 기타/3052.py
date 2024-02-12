# 나머지
import sys
input = sys.stdin.readline

ans = set()
for i in range(10):
    n = int(input())
    ans.add(n % 42)

print(len(ans))