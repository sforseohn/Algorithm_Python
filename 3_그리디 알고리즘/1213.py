# 팰린드롬 만들기
import sys
from collections import Counter
input = sys.stdin.readline

name = input().strip()
l = len(name)
alpha = sorted(Counter(name).items())

part1 = ''
mid = ''
for key, val in alpha:
    if val % 2 == 1:
        if not mid:
            mid = key
        else:
            print("I'm Sorry Hansoo")
            exit()
    
    part1 += key * (val // 2)

print(part1 + mid + part1[::-1])